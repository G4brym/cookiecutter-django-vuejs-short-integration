const BundleTracker = require("webpack-bundle-tracker");
const path = require("path");

function resolveRealPath(dir) {
  return path.join(__dirname, dir);
}

module.exports = {
  publicPath: "http://0.0.0.0:8080/",
  outputDir: "build/static/{{cookiecutter.vuejs_project_name}}",
  runtimeCompiler: true,
  filenameHashing: false,
  productionSourceMap: true,
  pages: {
    index: {
      entry: "{{cookiecutter.vuejs_project_name}}/main.js"
    }
  },

  chainWebpack: config => {
    config.externals({
      swaggeruibundle: "SwaggerUIBundle",
      swaggeruistandalonepreset: "SwaggerUIStandalonePreset"
    });

    config.output.filename(`${config.output.get("filename")}`);

    config.plugins.delete("html-index");
    config.plugins.delete("preload-index");
    config.plugins.delete("prefetch-index");

    const splitOptions = config.optimization.get("splitChunks");
    config.optimization.splitChunks(
      Object.assign({}, splitOptions, {
        maxAsyncRequests: 16,
        maxInitialRequests: 16,
        minChunks: 1,
        minSize: 30000,
        automaticNameDelimiter: "~",
        name: true,
        cacheGroups: {}
      })
    );

    config.plugin("BundleTracker").use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

    config.resolve.alias
      .set("__STATIC__", "static")
      .set("@views", resolveRealPath("{{cookiecutter.vuejs_project_name}}/views"))
      .set("@components", resolveRealPath("{{cookiecutter.vuejs_project_name}}/components"));

    config.module
      .rule("eslint")
      .use("eslint-loader")
      .options({
        fix: true
      });

    config.devServer
      .public("http://0.0.0.0:8080")
      .host("0.0.0.0")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }
};
