var Ros = require('../core/Ros');
var mixin = require('../mixin');

var tf = module.exports = {
    TFClient: require('./TFClient'),
    TF2Client: require('./TF2Client')
};

mixin(Ros, ['TFClient','TF2Client'], tf);
