const path = require("path");
const MiniCssExtractPlugins  = require("mini-css-extract-plugin");

module.exports = {
    entry: './src/js/index.js',
    mode: 'development',
    output:{
        filename:'index.js',
        path: path.resolve(__dirname, "../static/js"),
    },
    module: {
        rules:[
            {
                test:/\.(scss)$/,
                use:['style-loader','css-loader','sass-loader']
            } 
        ],
    },
    plugins: [
        new MiniCssExtractPlugins({
           filename: '../css/index.css', 
        }),
    ]
}


