(function(t){function a(a){for(var n,s,r=a[0],c=a[1],_=a[2],h=0,d=[];h<r.length;h++)s=r[h],Object.prototype.hasOwnProperty.call(l,s)&&l[s]&&d.push(l[s][0]),l[s]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(t[n]=c[n]);i&&i(a);while(d.length)d.shift()();return o.push.apply(o,_||[]),e()}function e(){for(var t,a=0;a<o.length;a++){for(var e=o[a],n=!0,r=1;r<e.length;r++){var c=e[r];0!==l[c]&&(n=!1)}n&&(o.splice(a--,1),t=s(s.s=e[0]))}return t}var n={},l={app:0},o=[];function s(a){if(n[a])return n[a].exports;var e=n[a]={i:a,l:!1,exports:{}};return t[a].call(e.exports,e,e.exports,s),e.l=!0,e.exports}s.m=t,s.c=n,s.d=function(t,a,e){s.o(t,a)||Object.defineProperty(t,a,{enumerable:!0,get:e})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,a){if(1&a&&(t=s(t)),8&a)return t;if(4&a&&"object"===typeof t&&t&&t.__esModule)return t;var e=Object.create(null);if(s.r(e),Object.defineProperty(e,"default",{enumerable:!0,value:t}),2&a&&"string"!=typeof t)for(var n in t)s.d(e,n,function(a){return t[a]}.bind(null,n));return e},s.n=function(t){var a=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(a,"a",a),a},s.o=function(t,a){return Object.prototype.hasOwnProperty.call(t,a)},s.p="/";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],c=r.push.bind(r);r.push=a,r=r.slice();for(var _=0;_<r.length;_++)a(r[_]);var i=c;o.push([0,"chunk-vendors"]),e()})({0:function(t,a,e){t.exports=e("56d7")},3194:function(t,a,e){},"56d7":function(t,a,e){"use strict";e.r(a);e("e260"),e("e6cf"),e("cca6"),e("a79d");var n=e("2b0e"),l=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{attrs:{id:"app"}},[e("Page")],1)},o=[],s=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"content"},[t.isLoading?e("div",{staticClass:"overlay"},[e("p",[t._v("Подождите, идет загрузка")])]):t.error.length?e("div",{staticClass:"overlay"},[e("p",[t._v(t._s(t.error))])]):t._e(),e("div",{staticClass:"row"},[e("div",{staticClass:"col col--left left"},[e("div",{staticClass:"left__title-card"},[t._v("Приложения/напрямую с FB (20%)")]),t._m(0),e("div",{staticClass:"table-wrapper"},[t.showDailyInfo?e("table",{staticClass:"left__table"},[e("thead",[e("tr",[e("th",{attrs:{colspan:"2"}},[t._v("Сумма за "+t._s((new Date).toLocaleString().split(",")[0]))])])]),e("tbody",[e("tr",[e("td",[t._v("Оборотка")]),e("td",[t._v(" "+t._s(t.totalDay[0].Day_Total_Gross_FB||0))])]),e("tr",[e("td",[t._v("Маржа")]),e("td",[t._v(" "+t._s(t.totalDay[0].Day_Total_Merjinalnost_FB||0))])]),e("tr",[e("td",[t._v("План")]),e("td",[t._v(" "+t._s(t.totalDay[0].Day_Plan_FB||0))])])])]):e("table",{staticClass:"left__table"},[t._m(1),e("tbody",[e("tr",[e("td",[t._v("Оборотка")]),e("td",[t._v(" "+t._s(t.totalMounth[0].Month_Total_Gross_FB||0))])]),e("tr",[e("td",[t._v("Маржа")]),e("td",[t._v(" "+t._s(t.totalMounth[0].Month_Total_Merjinalnost_FB||0))])]),e("tr",[e("td",[t._v("План")]),e("td",[t._v(" "+t._s(t.totalMounth[0].Month_Plan_FB||0))])])])])])]),e("div",{staticClass:"col col--right right"},[e("div",{staticClass:"table-wrapper"},[e("table",{staticClass:"table-main"},[e("thead",[e("tr",[e("th",{attrs:{rowspan:"2"}},[t._v("Рекламодатели")]),e("th",{attrs:{colspan:"3"}},[t._v("За "+t._s((new Date).toLocaleString().split(",")[0]))]),e("th",{attrs:{colspan:"3"}},[t._v("За месяц")])]),t._m(2)]),e("tbody",t._l(t.fb,(function(a,n){return e("tr",{key:n,class:{new:"true"===a.new}},[e("td",[t._v(t._s(a.reckl))]),e("td",[t._v(t._s(a.gross))]),e("td",[t._v(t._s(a.morja))]),e("td",{style:{color:t.calculatePercent(a.morja,a.plan_day)>99?"#FFFFFF":"#000000"}},[t._v(t._s(a.plan_day)+" ("+t._s(t.calculatePercent(a.morja,a.plan_day))+"%) "),e("span",{staticClass:"load",class:{"load--full":t.calculatePercent(a.morja,a.plan_day)>99},style:{width:t.calculatePercent(a.morja,a.plan_day)+"%"}})]),e("td",[t._v(t._s(a.grossMonth))]),e("td",[t._v(t._s(a.morjaMonth))]),e("td",{style:{color:t.calculatePercent(a.morjaMonth,a.plan_monthMonth)>99?"#FFFFFF":"#000000"}},[t._v(t._s(a.plan_monthMonth)+" ("+t._s(t.calculatePercent(a.morjaMonth,a.plan_monthMonth))+"%) "),e("span",{staticClass:"load",class:{"load--full":t.calculatePercent(a.morjaMonth,a.plan_monthMonth)>99},style:{width:t.calculatePercent(a.morjaMonth,a.plan_monthMonth)+"%"}})])])})),0)])])])]),e("div",{staticClass:"row"},[e("div",{staticClass:"col col--left left"},[e("div",{staticClass:"left__title-card"},[t._v("Схемы (75%)")]),t._m(3),e("div",{staticClass:"table-wrapper"},[t.showDailyInfo?e("table",{staticClass:"left__table"},[e("thead",[e("tr",[e("th",{attrs:{colspan:"2"}},[t._v("Сумма за "+t._s((new Date).toLocaleString().split(",")[0]))])])]),e("tbody",[e("tr",[e("td",[t._v("Оборотка")]),e("td",[t._v(t._s(t.totalDay[1].Day_Total_Gross_Sxema||0))])]),e("tr",[e("td",[t._v("Маржа")]),e("td",[t._v(t._s(t.totalDay[1].Day_Total_Merjinalnost_Sxema||0))])]),e("tr",[e("td",[t._v("План")]),e("td",[t._v(t._s(t.totalDay[1].Day_Plan_sxema||0))])])])]):e("table",{staticClass:"left__table"},[t._m(4),e("tbody",[e("tr",[e("td",[t._v("Оборотка")]),e("td",[t._v(t._s(t.totalMounth[1].Month_Total_Gross_sxema||0))])]),e("tr",[e("td",[t._v("Маржа")]),e("td",[t._v(t._s(t.totalMounth[1].Month_Total_Merjinalnost_sxema||0))])]),e("tr",[e("td",[t._v("План")]),e("td",[t._v(t._s(t.totalMounth[1].Month_Plan_sxema||0))])])])])])]),e("div",{staticClass:"col col--right right"},[e("div",{staticClass:"table-wrapper"},[e("table",{staticClass:"table-main"},[e("thead",[e("tr",[e("th",{attrs:{rowspan:"2"}},[t._v("Рекламодатели")]),e("th",{attrs:{colspan:"3"}},[t._v("За "+t._s((new Date).toLocaleString().split(",")[0]))]),e("th",{attrs:{colspan:"3"}},[t._v("За месяц")])]),t._m(5)]),e("tbody",t._l(t.scheme,(function(a,n){return e("tr",{key:n,class:{new:"true"===a.new}},[e("td",[t._v(t._s(a.reckl))]),e("td",[t._v(t._s(a.gross))]),e("td",[t._v(t._s(a.morja))]),e("td",{style:{color:t.calculatePercent(a.morja,a.plan_day)>99?"#FFFFFF":"#000000"}},[t._v(t._s(a.plan_day)+" ("+t._s(t.calculatePercent(a.morja,a.plan_day))+"%) "),e("span",{staticClass:"load",class:{"load--full":t.calculatePercent(a.morja,a.plan_day)>99},style:{width:t.calculatePercent(a.morja,a.plan_day)+"%"}})]),e("td",[t._v(t._s(a.grossMonth))]),e("td",[t._v(t._s(a.morjaMonth))]),e("td",{style:{color:t.calculatePercent(a.morjaMonth,a.plan_monthMonth)>99?"#FFFFFF":"#000000"}},[t._v(t._s(a.plan_monthMonth)+" ("+t._s(t.calculatePercent(a.morjaMonth,a.plan_monthMonth))+"%) "),e("span",{staticClass:"load",class:{"load--full":t.calculatePercent(a.morjaMonth,a.plan_monthMonth)>99},style:{width:t.calculatePercent(a.morjaMonth,a.plan_monthMonth)+"%"}})])])})),0)])])])]),e("div",{staticClass:"row"},[t._m(6),e("div",{staticClass:"col col--right right"},[e("div",{staticClass:"table-wrapper"},[e("table",{staticClass:"table-main"},[e("thead",[e("tr",[e("th",{attrs:{rowspan:"2"}},[t._v("Рекламодатели")]),e("th",{attrs:{colspan:"3"}},[t._v("За "+t._s((new Date).toLocaleString().split(",")[0]))]),e("th",{attrs:{colspan:"3"}},[t._v("За месяц")])]),t._m(7)]),e("tbody",t._l(t.other,(function(a,n){return e("tr",{key:n,class:{new:"true"===a.new}},[e("td",[t._v(t._s(a.reckl))]),e("td",[t._v(t._s(a.gross))]),e("td",[t._v(t._s(a.morja))]),e("td",{style:{color:t.calculatePercent(a.morja,a.plan_day)>99?"#FFFFFF":"#000000"}},[t._v(t._s(a.plan_day)+" ("+t._s(t.calculatePercent(a.morja,a.plan_day))+"%) "),e("span",{staticClass:"load",class:{"load--full":t.calculatePercent(a.morja,a.plan_day)>99},style:{width:t.calculatePercent(a.morja,a.plan_day)+"%"}})]),e("td",[t._v(t._s(a.grossMonth))]),e("td",[t._v(t._s(a.morjaMonth))]),e("td",{style:{color:t.calculatePercent(a.morjaMonth,a.plan_monthMonth)>99?"#FFFFFF":"#000000"}},[t._v(t._s(a.plan_monthMonth)+" ("+t._s(t.calculatePercent(a.morjaMonth,a.plan_monthMonth))+"%) "),e("span",{staticClass:"load",class:{"load--full":t.calculatePercent(a.morjaMonth,a.plan_monthMonth)>99},style:{width:t.calculatePercent(a.morjaMonth,a.plan_monthMonth)+"%"}})])])})),0)])])])])])},r=[function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"left__legend"},[e("div",{staticClass:"left__legend-item"},[t._v("NEW (30%)")]),e("div",{staticClass:"left__legend-item"},[t._v("OLD (70%)")])])},function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("thead",[e("tr",[e("th",{attrs:{colspan:"2"}},[t._v("Сумма за текущий месяц")])])])},function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("tr",[e("th",[t._v("Оборотка")]),e("th",[t._v("Маржа")]),e("th",[t._v("План")]),e("th",[t._v("Оборотка")]),e("th",[t._v("Маржа")]),e("th",[t._v("План")])])},function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"left__legend"},[e("div",{staticClass:"left__legend-item"},[t._v("NEW (30%)")]),e("div",{staticClass:"left__legend-item"},[t._v("OLD (70%)")])])},function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("thead",[e("tr",[e("th",{attrs:{colspan:"2"}},[t._v("Сумма за текущий месяц")])])])},function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("tr",[e("th",[t._v("Оборотка")]),e("th",[t._v("Маржа")]),e("th",[t._v("План")]),e("th",[t._v("Оборотка")]),e("th",[t._v("Маржа")]),e("th",[t._v("План")])])},function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"col col--left left"},[e("div",{staticClass:"left__title-card"},[t._v("Прочее (5%)")])])},function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("tr",[e("th",[t._v("Оборотка")]),e("th",[t._v("Маржа")]),e("th",[t._v("План")]),e("th",[t._v("Оборотка")]),e("th",[t._v("Маржа")]),e("th",[t._v("План")])])}],c=(e("7db0"),e("4160"),e("a9e3"),e("4fad"),e("d3b7"),e("159b"),e("2909")),_=e("3835"),i=e("bc3a"),h=e.n(i),d={data:function(){return{fb:[],scheme:[],other:[],timer:0,totalDay:[{},{}],totalMounth:[{},{}],showDailyInfo:!0,isLoading:!1,error:""}},methods:{switchTotalInfo:function(){var t=this,a=setTimeout((function(){t.showDailyInfo=!t.showDailyInfo,clearTimeout(a),t.switchTotalInfo()}),300500)},setData:function(t,a,e){var n=[];return Array.isArray(t[e])&&t[e].forEach((function(t){for(var l=Object.assign({},t),o=a[e].find((function(a){if(t.reckl===a.reckl)return a})),s=0,r=Object.entries(o);s<r.length;s++){var c=Object(_["a"])(r[s],2),i=c[0],h=c[1];l["".concat(i,"Month")]=h}n.push(l)})),n},calculatePercent:function(t,a){return Number(t)/Number(a)*100<=100?Math.round(Number(t)/Number(a)*100):100},loadData:function(){var t=this;this.isLoading=!0,this.error="",h.a.get("http://127.0.0.1:9988/Day_merj").then((function(a){for(var e=["FB","scheme","other"],n=0,l=e;n<l.length;n++){var o=l[n];t[o.toLowerCase()]=t.setData(a.data.Total_Day,a.data.TotalInformation_month,o)}return a.data})).then((function(a){t.totalDay=Object(c["a"])(a.Total_Day.Total),t.totalMounth=Object(c["a"])(a.TotalInformation_month.Total)})).catch((function(a){console.log(a),t.error="При загрузке данных произошла ошибка. Перезагрузите страницу"})).finally((function(){t.isLoading=!1}))},updateData:function(){var t=this;this.loadData(),0!==this.timer&&(clearInterval(this.timer),this.timer=0),this.timer=setInterval((function(){t.updateData()}),3e5)}},mounted:function(){this.updateData(),this.switchTotalInfo()}},u=d,v=(e("f321"),e("2877")),f=Object(v["a"])(u,s,r,!1,null,null,null),p=f.exports,m={name:"App",components:{Page:p}},y=m,b=Object(v["a"])(y,l,o,!1,null,null,null),M=b.exports;n["a"].config.productionTip=!1,new n["a"]({render:function(t){return t(M)}}).$mount("#app")},f321:function(t,a,e){"use strict";var n=e("3194"),l=e.n(n);l.a}});
//# sourceMappingURL=app.ca0379ff.js.map