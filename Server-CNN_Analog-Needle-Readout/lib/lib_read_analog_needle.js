require('@tensorflow/tfjs-node')
const tf = require('@tensorflow/tfjs')
var jpeg = require('jpeg-js');

var fs = require('fs');

var keras_model;

function load_image_to_tensor(image_name)
{
    var jpegData = fs.readFileSync(image_name);
    var rawImageData = jpeg.decode(jpegData);
    var rawImOhneAlpha = [];
    fLen = rawImageData.data.length;
    for (i = 0; i < fLen; i++) {
      if (((i+1) % 4) != 0)
      {
        rawImOhneAlpha.push(rawImageData.data[i]);
      }
    }
    var image_tensor = tf.tensor(rawImOhneAlpha, [1,32,32,3])
    const b = tf.scalar(255);
    image_tensor = image_tensor.div(b);         // normalize to 0..1
    return image_tensor;
}



const AnalogReadout = async function(image_name) 
{
    var pic_tensor = load_image_to_tensor(image_name);
    if (keras_model == undefined)
    {
        keras_model = await tf.loadLayersModel('file://lib/DL_model_analog_needle/model.json');
    }
    var pred = await keras_model.predict(pic_tensor);
    var result = await pred.as1D().dataSync()[0] * 10;
    return result;
}

module.exports = 
{
    AnalogReadout
}