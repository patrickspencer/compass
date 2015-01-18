/* jshint node:true */
'use strict';
// generated on 2014-12-26 using generator-gulp-webapp 0.2.0
var gulp = require('gulp');
var sass = require('gulp-sass');
var rev = require('gulp-rev');
var minifyCSS = require('gulp-minify-css');
var $ = require('gulp-load-plugins')();

gulp.task('copy', function(){
  gulp.src(['app/scripts/*'])
    .pipe(gulp.dest('dist/scripts/'));
  gulp.src(['bower_components/jquery/dist/jquery.min.js'])
    .pipe(gulp.dest('dist/scripts/vendor/'));
  gulp.src(['bower_components/bootstrap-sass-official/assets/javascripts/bootstrap.js'])
    .pipe(gulp.dest('dist/scripts/vendor/'));
  gulp.src(['app/images/*'])
    .pipe(gulp.dest('dist/images/'));
  gulp.src(['app/fonts/*'])
    .pipe(gulp.dest('dist/fonts/'));
});

gulp.task('sass', function () {
    gulp.src(['app/styles/**/*.scss'],{base: 'app'})
        .pipe(sass())
        .pipe(minifyCSS())
        .pipe(gulp.dest('dist/'))
        .pipe(rev.manifest())             // applies only changes to the manifest
        .pipe(gulp.dest('dist/'));
});

gulp.task('clean', require('del').bind(null, ['.tmp', 'dist']));

gulp.task('build', ['sass'], function () {
  return gulp.src('dist/**/*').pipe($.size({title: 'build', gzip: true}));
});

gulp.task('default', ['clean'], function () {
  gulp.start('build');
  gulp.start('copy');
});
