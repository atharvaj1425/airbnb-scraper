// client/next.config.mjs
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
import webpack from 'next/dist/compiled/webpack/webpack-lib.js';

export default {
  webpack: (config) => {
    // Provide a global "module" for loaders that expect it.
    config.plugins.push(
      new webpack.ProvidePlugin({
        module: require('module'),
      })
    );
    return config;
  },
};
