from pathlib import Path
import numpy as np
import math


def predict_and_evaluate(model, x_data, y_data, y_data_target=None):
    """
    Predict and compute deviation based on the model type

    Parameters:
    - model: model
    - x_data: Image data
    - y_data: expected labels (ana-class100: real values, ana-cont: sin/cos values)
    - y_data_target: ana-cont only: real values

    Returns:
    - predicted_val, expected_val, deviation_val
    """
    # Predict
    classes = model.predict(x_data.astype(np.float32), verbose=0)

    # Choose further processing depending on model output size
    if classes.shape[1] == 2:
        # ana-cont: Sin/Cos output (2 classes)
        predicted_sin = classes[:, 0]
        predicted_cos = classes[:, 1]

        predicted_val = (np.arctan2(predicted_sin, predicted_cos) / (2 * math.pi) % 1) * 10.0
        expected_val = np.array(y_data_target * 10.0)  # Scale target to match

    elif classes.shape[1] == 100:
        # ana-class100: Classification output (100 classes)
        predicted_val = np.argmax(classes, axis=1).reshape(-1) / 10
        expected_val = y_data

    else:
        raise ValueError(f"Unsupported model output. Classes: {classes.shape[1]}")

    # Compute deviation with wrap-around logic
    deviation_val = np.minimum(
        np.abs(predicted_val - expected_val),
        np.abs(predicted_val - (10.0 - expected_val))
    )

    # Round values for analysis or display
    predicted_val = np.round(predicted_val, 1)
    expected_val = np.round(expected_val, 1)
    deviation_val = np.round(deviation_val, 1)

    return predicted_val, expected_val, deviation_val


def get_false_predictions(expected_val, predicted_val, deviation_val, x_data, f_data, accepted_deviation=0.1):
    """
    Filters and returns false predictions sorted by deviation

    Args:
        expected_val (np.ndarray): Expected values
        predicted_val (np.ndarray): Model predicted values
        deviation_val (np.ndarray): Deviations between predicted and expected
        x_data (np.ndarray): Image data
        f_data (List[str]): File paths
        accepted_deviation (float): Max allowed deviation

    Returns:
        dict: False predictions sorted by deviation
    """
    false_predicted_mask = deviation_val > accepted_deviation

    # Filter arrays
    false_predicted_dev_values = deviation_val[false_predicted_mask]
    false_predicted_expected_values = expected_val[false_predicted_mask]
    false_predicted_pred_values = predicted_val[false_predicted_mask]
    false_predicted_images = x_data[false_predicted_mask]
    false_predicted_files = [Path(f).name for i, f in enumerate(f_data) if false_predicted_mask[i]]

    false_predicted_plt_labels = [
        f"Expected: {float(e):.1f}\n Predicted: {float(p):.1f}\n{Path(f).name[:-4][:20]}"
        for e, p, f in zip(
            false_predicted_expected_values,
            false_predicted_pred_values,
            np.array(f_data)[false_predicted_mask]
        )
    ]

    # Sort by deviation (descending)
    sorted_indices = np.argsort(false_predicted_dev_values)[::-1]

    return {
        "dev": false_predicted_dev_values[sorted_indices],
        "exp": false_predicted_expected_values[sorted_indices],
        "pred": false_predicted_pred_values[sorted_indices],
        "img": false_predicted_images[sorted_indices],
        "lbl": [false_predicted_plt_labels[i] for i in sorted_indices],
        "file": [false_predicted_files[i] for i in sorted_indices]
    }