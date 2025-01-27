var gulp = require("gulp");
var dirBase = require('browser-sync').create();
const browserSync = require("browser-sync");

gulp.task("serve", function() {
  browserSync.init({
    server: {
      baseDir: dirBase.resolve(__dirname, "./")
    },
    logLevel: "debug"
  });

  gulp.watch("*.html").on("change", browserSync.reload);
});
