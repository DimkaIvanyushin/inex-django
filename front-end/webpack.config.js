const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const merge = require('webpack-merge');
const pug = require('./webpack/pug');
const devserver = require('./webpack/devserver');
const sass = require('./webpack/sass');
const styl = require('./webpack/styl');
const css = require('./webpack/css');
const wow = require('./webpack/wow');
const extractCSS = require('./webpack/css.extract');
const uglifyJS = require('./webpack/js.uglify');
const images = require('./webpack/images');

const PATHS = {
    source: path.join(__dirname, 'frontend'),
    build: path.join(__dirname, 'build')
};

const common = merge([
    {
        entry: {
            'index': PATHS.source + '/pages/index/index.js',
            'service': PATHS.source + '/pages/service/index.js',
            'services-list': PATHS.source + '/pages/services-list/index.js',
        },
        output: {
            path: PATHS.build,
            filename: './static/js/[name].js',
        },
        plugins: [
            new HtmlWebpackPlugin({
                filename: 'templates/index.html',
                chunks: ['index', 'common'],
                template: PATHS.source + '/pages/index/index.pug'
            }),
            new HtmlWebpackPlugin({
                filename: 'templates/service.html',
                chunks: ['service', 'common'],
                template: PATHS.source + '/pages/service/index.pug'
            }),
            new HtmlWebpackPlugin({
                filename: 'templates/services-list.html',
                chunks: ['services-list', 'common'],
                template: PATHS.source + '/pages/services-list/index.pug'
            }),
            new webpack.optimize.CommonsChunkPlugin({
                name: 'common'
            }),
            new webpack.ProvidePlugin({
                $: 'jquery',
                jQuery: 'jquery'
            }),
        ]
    },
    pug(),
    images()
]);

module.exports = function (env) {
    if (env === 'production') {
        return merge([
            common,
            extractCSS(),
            uglifyJS(),
            wow()
        ]);
    }
    if (env === 'development') {
        return merge([
            common,
            devserver(),
            wow(),
            styl(),
            sass(),
            css()
        ])
    }
};










