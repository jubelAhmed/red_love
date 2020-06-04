const path = require("path");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const exclusions = /node_modules/;

module.exports = [
  {
    entry: {
      app: './src/js/index.js',
    },
    output: {
      path: path.resolve(__dirname, "../static/js"),
      publicPath: "/static/",
      filename: "[name].js",
      chunkFilename: "[id]-[chunkhash].js",
    },
    devServer: {
      port: 8081,
      writeToDisk: true,
    },
    module: {
      rules: [
        {
          test: /.*/,
          include: path.resolve(__dirname, "../static/images"),
          exclude: exclusions,
          options: {
            context: path.resolve(__dirname, "assets/"),
            name: "[path][name].[ext]",
          },
          loader: "file-loader",
        },
        {
          test: /\.css$/,
          exclude: exclusions,
          use: [
            MiniCssExtractPlugin.loader,
            { loader: "css-loader" },
          ],
        },
        {
            test:/\.(scss)$/,
            use:[MiniCssExtractPlugin.loader,'css-loader','sass-loader']
        },
      ],
    },
    plugins: [
      new CleanWebpackPlugin({ cleanStaleWebpackAssets: false }),
      new MiniCssExtractPlugin({
        filename: '../css/index.css', 
     }),
    ],
  },
];
