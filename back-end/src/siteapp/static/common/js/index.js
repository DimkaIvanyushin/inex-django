webpackJsonp([0],[
/* 0 */,
/* 1 */,
/* 2 */,
/* 3 */,
/* 4 */,
/* 5 */,
/* 6 */,
/* 7 */,
/* 8 */,
/* 9 */,
/* 10 */,
/* 11 */,
/* 12 */,
/* 13 */,
/* 14 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 15 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 16 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 17 */,
/* 18 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 19 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 20 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 21 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 22 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 23 */,
/* 24 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 25 */,
/* 26 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 27 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 28 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 29 */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),
/* 30 */,
/* 31 */,
/* 32 */,
/* 33 */,
/* 34 */
/***/ (function(module, exports, __webpack_require__) {

/* WEBPACK VAR INJECTION */(function($) {$(document).ready(function () {

    var $mainMenu = $('.main-menu');
    var menuOffsetTop = $mainMenu.offset().top;
    var check = false;

    var $section_slider = $('section.slider');
    var $slide = $('section.slider .carousel-item .item');

    function parallaxScroll() {
        var scrolled = $(window).scrollTop();
        $slide.css('background-position-y', (0 + ((scrolled - 150) * .50)) + 'px');
    }

    $(window).bind('scroll', function () {
        if ($(window).scrollTop() > menuOffsetTop) {

            parallaxScroll()

            if (!check) {

                $section_slider.css("top", "77px");
                $mainMenu.addClass('fixed-top');

                $mainMenu.find('#navbarSupportedContent')
                    .find('ul')
                    .removeClass('hide')
                    .addClass('show')
                    .find('li.search')
                    .removeClass('ml-auto');

                $mainMenu.find('.logo-dt')
                    .removeClass('hide')
                    .addClass('show')

                check = true;
            }
        } else {
            if (check) {
                $section_slider.css("top", "0");
                $mainMenu.removeClass('fixed-top');

                $mainMenu.find('#navbarSupportedContent')
                    .find('ul')
                    .removeClass('show')
                    .addClass('hide')
                    .find('li.search')
                    .addClass('ml-auto');

                $mainMenu.find('.logo-dt')
                    .removeClass('show')
                    .addClass('hide')

                check = false;
            }
        }
    });

});
/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__(13)))

/***/ }),
/* 35 */,
/* 36 */,
/* 37 */,
/* 38 */,
/* 39 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_bootstrap__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_bootstrap___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_bootstrap__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_bootstrap_dist_css_bootstrap_min_css__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_bootstrap_dist_css_bootstrap_min_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_bootstrap_dist_css_bootstrap_min_css__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__fortawesome_fontawesome_free_js_fontawesome__ = __webpack_require__(3);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__fortawesome_fontawesome_free_js_fontawesome___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__fortawesome_fontawesome_free_js_fontawesome__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__fortawesome_fontawesome_free_js_solid__ = __webpack_require__(5);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__fortawesome_fontawesome_free_js_solid___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3__fortawesome_fontawesome_free_js_solid__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__fortawesome_fontawesome_free_js_regular__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__fortawesome_fontawesome_free_js_regular___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_4__fortawesome_fontawesome_free_js_regular__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__fortawesome_fontawesome_free_js_brands__ = __webpack_require__(2);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__fortawesome_fontawesome_free_js_brands___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_5__fortawesome_fontawesome_free_js_brands__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_animate_css__ = __webpack_require__(9);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_animate_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_6_animate_css__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7_wow_js_dist_wow_js__ = __webpack_require__(12);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7_wow_js_dist_wow_js___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_7_wow_js_dist_wow_js__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8_normalize_css__ = __webpack_require__(11);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8_normalize_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_8_normalize_css__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__index_styl__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__index_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_9__index_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__components_header_top_header_top_styl__ = __webpack_require__(21);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__components_header_top_header_top_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_10__components_header_top_header_top_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__components_header_menu_header_menu_styl__ = __webpack_require__(8);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__components_header_menu_header_menu_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_11__components_header_menu_header_menu_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__components_slider_slider_styl__ = __webpack_require__(27);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__components_slider_slider_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_12__components_slider_slider_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__components_about_us_about_us_styl__ = __webpack_require__(14);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__components_about_us_about_us_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_13__components_about_us_about_us_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__components_small_features_small_features_styl__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__components_small_features_small_features_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_14__components_small_features_small_features_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__components_alert_cta_alert_cta_styl__ = __webpack_require__(16);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__components_alert_cta_alert_cta_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_15__components_alert_cta_alert_cta_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__components_services_services_styl__ = __webpack_require__(26);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__components_services_services_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_16__components_services_services_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__components_prices_prices_styl__ = __webpack_require__(24);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__components_prices_prices_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_17__components_prices_prices_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_18__components_recall_recall_styl__ = __webpack_require__(15);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_18__components_recall_recall_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_18__components_recall_recall_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_19__components_alert_mdl_alert_mdl_styl__ = __webpack_require__(18);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_19__components_alert_mdl_alert_mdl_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_19__components_alert_mdl_alert_mdl_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_20__components_last_blog_last_blog_styl__ = __webpack_require__(22);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_20__components_last_blog_last_blog_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_20__components_last_blog_last_blog_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_21__components_contact_us_contact_us_styl__ = __webpack_require__(19);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_21__components_contact_us_contact_us_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_21__components_contact_us_contact_us_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_22__components_contact_contact_styl__ = __webpack_require__(20);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_22__components_contact_contact_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_22__components_contact_contact_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_23__components_footer_main_footer_styl__ = __webpack_require__(7);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_23__components_footer_main_footer_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_23__components_footer_main_footer_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_24__components_parallax_slider__ = __webpack_require__(34);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_24__components_parallax_slider___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_24__components_parallax_slider__);
// import bootstrap 4


// import fontawesome 




// import wow.js


// import normalize.css


// import style
















// import '../../components/header-menu/header-menu.js';


new __WEBPACK_IMPORTED_MODULE_7_wow_js_dist_wow_js___default.a().init();

/***/ })
],[39]);