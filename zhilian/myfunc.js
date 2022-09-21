// function func_r(t, e, n) {
//     function func_66(t, e, n) {
//         t.exports = function (t, e) {
//             return function () {
//                 for (var n = new Array(arguments.length), r = 0; r < n.length; r++) n[r] = arguments[r];
//                 return t.apply(e, n)
//             }
//         }
//     }
//
//     function func_131(t, e) {
//         function n(t) {
//             return !!t.constructor && "function" == typeof t.constructor.isBuffer && t.constructor.isBuffer(t)
//         }
//
//         t.exports = function (t) {
//             return null != t && (n(t) || function (t) {
//                 return "function" == typeof t.readFloatLE && "function" == typeof t.slice && n(t.slice(0, 0))
//             }(t) || !!t._isBuffer)
//         }
//     }
//
//     var r = func_66, o = func_131, i = Object.prototype.toString;
//
//     function a(t) {
//         return "[object Array]" === i.call(t)
//     }
//
//     function s(t) {
//         return null !== t && "object" == typeof t
//     }
//
//     function c(t) {
//         return "[object Function]" === i.call(t)
//     }
//
//     function u(t, e) {
//         if (null != t) if ("object" == typeof t || a(t) || (t = [t]), a(t)) for (var n = 0, r = t.length; n < r; n++) e.call(null, t[n], n, t); else for (var o in t) Object.prototype.hasOwnProperty.call(t, o) && e.call(null, t[o], o, t)
//     }
//
//     t.exports = {
//         isArray: a,
//         isArrayBuffer: function (t) {
//             return "[object ArrayBuffer]" === i.call(t)
//         },
//         isBuffer: o, isFormData: function (t) {
//             return "undefined" != typeof FormData && t instanceof FormData
//         },
//         isArrayBufferView: function (t) {
//             return "undefined" != typeof ArrayBuffer && ArrayBuffer.isView ? ArrayBuffer.isView(t) : t && t.buffer && t.buffer instanceof ArrayBuffer
//         },
//         isString: function (t) {
//             return "string" == typeof t
//         },
//         isNumber: function (t) {
//             return "number" == typeof t
//         },
//         isObject: s, isUndefined: function (t) {
//             return void 0 === t
//         },
//         isDate: function (t) {
//             return "[object Date]" === i.call(t)
//         },
//         isFile: function (t) {
//             return "[object File]" === i.call(t)
//         }, isBlob: function (t) {
//             return "[object Blob]" === i.call(t)
//         }, isFunction: c, isStream: function (t) {
//             return s(t) && c(t.pipe)
//         }, isURLSearchParams: function (t) {
//             return "undefined" != typeof URLSearchParams && t instanceof URLSearchParams
//         }, isStandardBrowserEnv: function () {
//             return ("undefined" == typeof navigator || "ReactNative" !== navigator.product) && ("undefined" != typeof window && "undefined" != typeof document)
//         }, forEach: u, merge: function t() {
//             var e = {};
//
//             function n(n, r) {
//                 "object" == typeof e[r] && "object" == typeof n ? e[r] = t(e[r], n) : e[r] = n
//             }
//
//             for (var r = 0, o = arguments.length; r < o; r++) u(arguments[r], n);
//             return e
//         }, extend: function (t, e, n) {
//             return u(e, (function (e, o) {
//                 t[o] = n && "function" == typeof e ? r(e, n) : e
//             })), t
//         }, trim: function (t) {
//             return t.replace(/^\s*/, "").replace(/\s*$/, "")
//         }
//     }
// }


function isString(t) {
    return "string" == typeof t
}

function isNumber(t) {
    return "number" == typeof t
}

function write(t, e, n, o, i, a) {
    var s = [];
    s.push(t + "=" + encodeURIComponent(e)),
    isNumber(n) && s.push("expires=" + new Date(n).toGMTString()),
    isString(o) && s.push("path=" + o),
    isString(i) && s.push("domain=" + i),
    !0 === a && s.push("secure"),
        // document.cookie = s.join("; ")
    console.log('cookie', s.join("; "));
}

function i(e, n, i, a) {
    a = a || {};
    console.log('aaaaaaaaa')
    // if ("undefined" != typeof document) {
        console.log('bbbbbbb')
        "number" == typeof (i = t({path: "/"}, {}, i)).expires && (i.expires = new Date(1 * new Date + 864e5 * i.expires)), i.expires = i.expires ? i.expires.toUTCString() : "";
        try {
            var s = JSON.stringify(n);
            /^[\{\[]/.test(s) && (n = s)
        } catch (t) {
        }
        n = write ? write(n, e) : encodeURIComponent(String(n)).replace(/%(23|24|26|2B|3A|3C|3E|3D|2F|3F|40|5B|5D|5E|60|7B|7D|7C)/g, decodeURIComponent), e = (e = (e = a.encodeKey ? encodeURIComponent(String(e)) : String(e)).replace(/%(23|24|26|2B|5E|60|7C)/g, decodeURIComponent)).replace(/[\(\)]/g, escape);
        var c = "";
        for (var u in i) i[u] && (c += "; " + u, !0 !== i[u] && (c += "=" + i[u].split(";")[0]));
        // return document.cookie = e + "=" + n + c
    console.log('my cookie',e + "=" + n + c)
    // }
}

function t() {
    for (var t = 0, e = {}; t < arguments.length; t++) {
        var n = arguments[t];
        for (var r in n) e[r] = n[r]
    }
    console.log(e)
    return e
}
// "rt", {domain: ".zhaopin.com"}
var e = "rt", n = {domain: ".zhaopin.com"}
var result = i(e, "", t(n, {expires: -1}))
console.log(result)