const path = require('path');

module.exports = {
  mode: 'development',
  entry: './static/js/upload.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static'),
  },
  resolve: {
    modules: [
      'node_modules',
    ],
    alias: {
        uuid: 'uuid'
    }
  },
};
