webpackJsonp([2],{

/***/ 0:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 1:
/***/ (function(module, exports, __webpack_require__) {

/* WEBPACK VAR INJECTION */(function($) {$(document).ready(function () {

    var $breadcrumbs = $('section.breadcrumbs');

    var $navbar = $('.navbar');

    $navbar.addClass('fixed-top').find('.logo-dt').addClass('show')
    $navbar.addClass('fixed-top').find('.navbar-nav').addClass('show')
    

    $(window).bind('scroll',function(e){
        parallaxScroll();
    });
     
    function parallaxScroll(){
        var scrolled = $(window).scrollTop();
        $breadcrumbs.css('background-position-y',(0+(scrolled*.70))+'px');
    }
});

/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__(13)))

/***/ }),

/***/ 15:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 23:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 30:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 40:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* WEBPACK VAR INJECTION */(function($) {/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_bootstrap__ = __webpack_require__(6);
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
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__index_styl__ = __webpack_require__(30);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__index_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_9__index_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__components_header_menu_header_menu_styl__ = __webpack_require__(8);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__components_header_menu_header_menu_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_10__components_header_menu_header_menu_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__components_breadcrumbs_breadcrumbs_styl__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__components_breadcrumbs_breadcrumbs_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_11__components_breadcrumbs_breadcrumbs_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__components_recall_recall_styl__ = __webpack_require__(15);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__components_recall_recall_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_12__components_recall_recall_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__components_per_char_per_char_styl__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__components_per_char_per_char_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_13__components_per_char_per_char_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__components_footer_main_footer_styl__ = __webpack_require__(7);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__components_footer_main_footer_styl___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_14__components_footer_main_footer_styl__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__components_parallax_bred_js__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__components_parallax_bred_js___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_15__components_parallax_bred_js__);
// import bootstrap 4


// import fontawesome 




// import wow.js


// import normalize.css


// import style










// import '../../components/breadcrumbs/breadcrumbs.js';
// import '../../components/header-menu/header-menu.js';
new __WEBPACK_IMPORTED_MODULE_7_wow_js_dist_wow_js___default.a().init();

$(document).ready(function () {

    const $section_tabs = $('section.tabs');

    $('.more-button').click(function () {
        $section_tabs.toggle('show');
    });

});
/* WEBPACK VAR INJECTION */}.call(__webpack_exports__, __webpack_require__(13)))

/***/ })

},[40]);