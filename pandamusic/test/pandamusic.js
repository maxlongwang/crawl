function ho() {
    if (!ro && null !== to) {
        ro = !0;
        var e = 0;
        try {
            var t = to;
            co(99, (function () {
                for (; e < t.length; e++) {
                    var n = t[e];
                    do {
                        n = n(!0)
                    } while (null !== n)
                }
            }
            )),
                to = null
        } catch (t) {
            throw null !== to && (to = to.slice(e + 1)),
            Ui(qi, fo),
            t
        } finally {
            ro = !1
        }
    }
}

function ao() {
    switch (Yi()) {
        case qi:
            return 99;
        case Ki:
            return 98;
        case Qi:
            return 97;
        case Zi:
            return 96;
        case Xi:
            return 95;
        default:
            throw Error(a(332))
    }
}



function Gc(e) {
    var t = ao();
    return co(99, Yc.bind(null, e, t)),
        null
}

function Ac(e) {
    var t = e.lastExpiredTime;
    if (t = 0 !== t ? t : 1073741823,
        0 != (48 & Js))
        throw Error(a(327));
    if (Kc(),
        e === ec && t === nc || Lc(e, t),
        null !== tc) {
        var n = Js;
        Js |= 16;
        for (var r = zc(); ;)
            try {
                Bc();
                break
            } catch (t) {
                jc(e, t)
            }
        if (wo(),
            Js = n,
            Hs.current = r,
            1 === rc)
            throw n = ic,
            Lc(e, t),
            pl(e, t),
            Ic(e),
            n;
        if (null !== tc)
            throw Error(a(261));
        e.finishedWork = e.current.alternate,
            e.finishedExpirationTime = t,
            ec = null,
            Gc(e),
            Ic(e)
    }
    return null
}
function hl(e, t) {
    var n = e.firstSuspendedTime;
    return e = e.lastSuspendedTime,
        0 !== n && n >= t && e <= t
}

function st(e) {
    var t = e
        , n = e;
    if (e.alternate)
        for (; t.return;)
            t = t.return;
    else {
        e = t;
        do {
            0 != (1026 & (t = e).effectTag) && (n = t.return),
                e = t.return
        } while (e)
    }
    return 3 === t.tag ? n : null
}

function cn(e, t, n, r) {
    nn(tn, ln.bind(null, e, t, n, r))
}

function Sc(e) {
    var t = e.lastExpiredTime;
    if (0 !== t)
        return t;
    if (!hl(e, t = e.firstPendingTime))
        return t;
    var n = e.lastPingedTime;
    return 2 >= (e = n > (e = e.nextKnownPendingLevel) ? n : e) && t !== e ? 0 : e
}
function Ic(e) {
    if (0 !== e.lastExpiredTime)
        e.callbackExpirationTime = 1073741823,
            e.callbackPriority = 99,
            e.callbackNode = uo(Ac.bind(null, e));
    else {
        var t = Sc(e)
            , n = e.callbackNode;
        if (0 === t)
            null !== n && (e.callbackNode = null,
                e.callbackExpirationTime = 0,
                e.callbackPriority = 90);
        else {
            var r = Ec();
            if (1073741823 === t ? r = 99 : 1 === t || 2 === t ? r = 95 : r = 0 >= (r = 10 * (1073741821 - t) - 10 * (1073741821 - r)) ? 99 : 250 >= r ? 98 : 5250 >= r ? 97 : 95,
                null !== n) {
                var i = e.callbackPriority;
                if (e.callbackExpirationTime === t && i >= r)
                    return;
                n !== $i && Vi(n)
            }
            e.callbackExpirationTime = t,
                e.callbackPriority = r,
                t = 1073741823 === t ? uo(Ac.bind(null, e)) : lo(r, kc.bind(null, e), {
                    timeout: 10 * (1073741821 - t) - oo()
                }),
                e.callbackNode = t
        }
    }
}

function Wc(e) {
    var t = e.expirationTime;
    return t > (e = e.childExpirationTime) ? t : e
}
function Or(e) {
    var t = e && e.nodeName && e.nodeName.toLowerCase();
    return "input" === t ? !!Tr[e.type] : "textarea" === t
}

function or() {
    return !1
}

function wt(e) {
    e.topLevelType = null,
    e.nativeEvent = null,
    e.targetInst = null,
    e.ancestors.length = 0,
    10 > bt.length && bt.push(e)
}


function Yc(e, t) {
    do {
        Kc()
    } while (null !== vc);
    if (0 != (48 & Js))
        throw Error(a(327));
    var n = e.finishedWork
        , r = e.finishedExpirationTime;
    if (null === n)
        return null;
    if (e.finishedWork = null,
        e.finishedExpirationTime = 0,
        n === e.current)
        throw Error(a(177));
    e.callbackNode = null,
        e.callbackExpirationTime = 0,
        e.callbackPriority = 90,
        e.nextKnownPendingLevel = 0;
    var i = Wc(n);
    if (e.firstPendingTime = i,
        r <= e.lastSuspendedTime ? e.firstSuspendedTime = e.lastSuspendedTime = e.nextKnownPendingLevel = 0 : r <= e.firstSuspendedTime && (e.firstSuspendedTime = r - 1),
        r <= e.lastPingedTime && (e.lastPingedTime = 0),
        r <= e.lastExpiredTime && (e.lastExpiredTime = 0),
        e === ec && (tc = ec = null,
            nc = 0),
        1 < n.effectTag ? null !== n.lastEffect ? (n.lastEffect.nextEffect = n,
            i = n.firstEffect) : i = n : i = n.firstEffect,
        null !== i) {
        var o = Js;
        Js |= 32,
            Us.current = null,
            An = rn;
        var s = Cn();
        if (Tn(s)) {
            if ("selectionStart" in s)
                var c = {
                    start: s.selectionStart,
                    end: s.selectionEnd
                };
            else
                e: {
                    var l = (c = (c = s.ownerDocument) && c.defaultView || window).getSelection && c.getSelection();
                    if (l && 0 !== l.rangeCount) {
                        c = l.anchorNode;
                        var u = l.anchorOffset
                            , d = l.focusNode;
                        l = l.focusOffset;
                        try {
                            c.nodeType,
                                d.nodeType
                        } catch (e) {
                            c = null;
                            break e
                        }
                        var f = 0
                            , h = -1
                            , p = -1
                            , g = 0
                            , m = 0
                            , v = s
                            , y = null;
                        t: for (; ;) {
                            for (var b; v !== c || 0 !== u && 3 !== v.nodeType || (h = f + u),
                                v !== d || 0 !== l && 3 !== v.nodeType || (p = f + l),
                                3 === v.nodeType && (f += v.nodeValue.length),
                                null !== (b = v.firstChild);)
                                y = v,
                                    v = b;
                            for (; ;) {
                                if (v === s)
                                    break t;
                                if (y === c && ++g === u && (h = f),
                                    y === d && ++m === l && (p = f),
                                    null !== (b = v.nextSibling))
                                    break;
                                y = (v = y).parentNode
                            }
                            v = b
                        }
                        c = -1 === h || -1 === p ? null : {
                            start: h,
                            end: p
                        }
                    } else
                        c = null
                }
            c = c || {
                start: 0,
                end: 0
            }
        } else
            c = null;
        Dn = {
            activeElementDetached: null,
            focusedElem: s,
            selectionRange: c
        },
            rn = !1,
            fc = i;
        do {
            try {
                qc()
            } catch (e) {
                if (null === fc)
                    throw Error(a(330));
                Xc(fc, e),
                    fc = fc.nextEffect
            }
        } while (null !== fc);
        fc = i;
        do {
            try {
                for (s = e,
                    c = t; null !== fc;) {
                    var w = fc.effectTag;
                    if (16 & w && Ke(fc.stateNode, ""),
                        128 & w) {
                        var _ = fc.alternate;
                        if (null !== _) {
                            var M = _.ref;
                            null !== M && ("function" == typeof M ? M(null) : M.current = null)
                        }
                    }
                    switch (1038 & w) {
                        case 2:
                            As(fc),
                                fc.effectTag &= -3;
                            break;
                        case 6:
                            As(fc),
                                fc.effectTag &= -3,
                                Ls(fc.alternate, fc);
                            break;
                        case 1024:
                            fc.effectTag &= -1025;
                            break;
                        case 1028:
                            fc.effectTag &= -1025,
                                Ls(fc.alternate, fc);
                            break;
                        case 4:
                            Ls(fc.alternate, fc);
                            break;
                        case 8:
                            Ps(s, u = fc, c),
                                Is(u)
                    }
                    fc = fc.nextEffect
                }
            } catch (e) {
                if (null === fc)
                    throw Error(a(330));
                Xc(fc, e),
                    fc = fc.nextEffect
            }
        } while (null !== fc);
        if (M = Dn,
            _ = Cn(),
            w = M.focusedElem,
            c = M.selectionRange,
            _ !== w && w && w.ownerDocument && En(w.ownerDocument.documentElement, w)) {
            null !== c && Tn(w) && (_ = c.start,
                void 0 === (M = c.end) && (M = _),
                "selectionStart" in w ? (w.selectionStart = _,
                    w.selectionEnd = Math.min(M, w.value.length)) : (M = (_ = w.ownerDocument || document) && _.defaultView || window).getSelection && (M = M.getSelection(),
                        u = w.textContent.length,
                        s = Math.min(c.start, u),
                        c = void 0 === c.end ? s : Math.min(c.end, u),
                        !M.extend && s > c && (u = c,
                            c = s,
                            s = u),
                        u = xn(w, s),
                        d = xn(w, c),
                        u && d && (1 !== M.rangeCount || M.anchorNode !== u.node || M.anchorOffset !== u.offset || M.focusNode !== d.node || M.focusOffset !== d.offset) && ((_ = _.createRange()).setStart(u.node, u.offset),
                            M.removeAllRanges(),
                            s > c ? (M.addRange(_),
                                M.extend(d.node, d.offset)) : (_.setEnd(d.node, d.offset),
                                    M.addRange(_))))),
                _ = [];
            for (M = w; M = M.parentNode;)
                1 === M.nodeType && _.push({
                    element: M,
                    left: M.scrollLeft,
                    top: M.scrollTop
                });
            for ("function" == typeof w.focus && w.focus(),
                w = 0; w < _.length; w++)
                (M = _[w]).element.scrollLeft = M.left,
                    M.element.scrollTop = M.top
        }
        rn = !!An,
            Dn = An = null,
            e.current = n,
            fc = i;
        do {
            try {
                for (w = e; null !== fc;) {
                    var x = fc.effectTag;
                    if (36 & x && Os(w, fc.alternate, fc),
                        128 & x) {
                        _ = void 0;
                        var E = fc.ref;
                        if (null !== E) {
                            var C = fc.stateNode;
                            switch (fc.tag) {
                                case 5:
                                    _ = C;
                                    break;
                                default:
                                    _ = C
                            }
                            "function" == typeof E ? E(_) : E.current = _
                        }
                    }
                    fc = fc.nextEffect
                }
            } catch (e) {
                if (null === fc)
                    throw Error(a(330));
                Xc(fc, e),
                    fc = fc.nextEffect
            }
        } while (null !== fc);
        fc = null,
            eo(),
            Js = o
    } else
        e.current = n;
    if (mc)
        mc = !1,
            vc = e,
            yc = t;
    else
        for (fc = i; null !== fc;)
            t = fc.nextEffect,
                fc.nextEffect = null,
                fc = t;
    if (0 === (t = e.firstPendingTime) && (gc = null),
        1073741823 === t ? e === _c ? wc++ : (wc = 0,
            _c = e) : wc = 0,
        "function" == typeof el && el(n.stateNode, r),
        Ic(e),
        hc)
        throw hc = !1,
        e = pc,
        pc = null,
        e;
    return 0 != (8 & Js) || fo(),
        null
}

function un(e, t, n, r) {
    if (null !== (n = Vn(n = vt(r)))) {
        var i = st(n);
        if (null === i)
            n = null;
        else {
            var o = i.tag;
            if (13 === o) {
                if (null !== (n = ct(i)))
                    return n;
                n = null
            } else if (3 === o) {
                if (i.stateNode.hydrate)
                    return 3 === i.tag ? i.stateNode.containerInfo : null;
                n = null
            } else
                i !== n && (n = null)
        }
    }
    e = _t(e, r, n, t);
    try {
        U(Mt, e)
    } finally {
        wt(e)
    }
    return null
}

function _t(e, t, n, r) {
    if (bt.length) {
        var i = bt.pop();
        return i.topLevelType = e,
            i.eventSystemFlags = r,
            i.nativeEvent = t,
            i.targetInst = n,
            i
    }
    return {
        topLevelType: e,
        eventSystemFlags: r,
        nativeEvent: t,
        targetInst: n,
        ancestors: []
    }
}

function cr(e) {
    if (!(e instanceof this))
        throw Error(a(279));
    e.destructor(),
        10 > this.eventPool.length && this.eventPool.push(e)
}

function H() {
    null === k && null === A || (z(),
        P())
}

z = function () {
    0 == (49 & Js) && (Dc(),
        Kc())
}


function U(e, t, n) {
    if (B)
        return e(t, n);
    B = !0;
    try {
        return R(e, t, n)
    } finally {
        B = !1,
            H()
    }
}

R = function (e, t) {
    var n = Js;
    Js |= 2;
    try {
        return e(t)
    } finally {
        0 === (Js = n) && fo()
    }
}

function mt(e) {
    if (null !== e && (pt = ft(pt, e)),
        e = pt,
        pt = null,
        e) {
        if (ht(e, gt),
            pt)
            throw Error(a(95));
        if (u)
            throw e = d,
            u = !1,
            d = null,
            e
    }
}

function Mt(e) {
    var t = e.targetInst
        , n = t;
    do {
        if (!n) {
            e.ancestors.push(n);
            break
        }
        var r = n;
        if (3 === r.tag)
            r = r.stateNode.containerInfo;
        else {
            for (; r.return;)
                r = r.return;
            r = 3 !== r.tag ? null : r.stateNode.containerInfo
        }
        if (!r)
            break;
        5 !== (t = n.tag) && 6 !== t || e.ancestors.push(n),
            n = Vn(r)
    } while (n);
    for (n = 0; n < e.ancestors.length; n++) {
        t = e.ancestors[n];
        var i = vt(e.nativeEvent);
        r = e.topLevelType;
        var o = e.nativeEvent
            , a = e.eventSystemFlags;
        0 === n && (a |= 64);
        for (var s = null, c = 0; c < x.length; c++) {
            var l = x[c];
            l && (l = l.extractEvents(r, t, o, i, a)) && (s = ft(s, l))
        }
        mt(s)
    }
}

function sr(e, t, n, r) {
    if (this.eventPool.length) {
        var i = this.eventPool.pop();
        return this.call(i, e, t, n, r),
            i
    }
    return new this(e, t, n, r)
}

function ht(e, t, n) {
    Array.isArray(e) ? e.forEach(t, n) : e && t.call(n, e)
}

function Jn(e) {
    ht(e, Zn)
}


function vt(e) {
    return (e = e.target || e.srcElement || window).correspondingUseElement && (e = e.correspondingUseElement),
        3 === e.nodeType ? e.parentNode : e
}

function ar(e, t, n, r) {
    for (var i in this.dispatchConfig = e,
        this._targetInst = t,
        this.nativeEvent = n,
        e = this.constructor.Interface)
        e.hasOwnProperty(i) && ((t = e[i]) ? this[i] = t(n) : "target" === i ? this.target = r : this[i] = n[i]);
    return this.isDefaultPrevented = (null != n.defaultPrevented ? n.defaultPrevented : !1 === n.returnValue) ? ir : or,
        this.isPropagationStopped = or,
        this
}

function Yr() {
    return Gr
}



function Vn(e) {
    var t = e[Bn];
    if (t)
        return t;
    for (var n = e.parentNode; n;) {
        if (t = n[Un] || n[Bn]) {
            if (n = t.alternate,
                null !== t.child || null !== n && null !== n.child)
                for (e = Rn(e); null !== e;) {
                    if (n = e[Bn])
                        return n;
                    e = Rn(e)
                }
            return t
        }
        n = (e = n).parentNode
    }
    return null
}


function e(e, t, n, r) {
    if (rn)
        if (0 < St.length && -1 < Lt.indexOf(e))
            e = Rt(null, e, t, n, r),
                St.push(e);
        else {
            var i = un(e, t, n, r);
            if (null === i)
                Ft(e, r);
            else if (-1 < Lt.indexOf(e))
                e = Rt(i, e, t, n, r),
                    St.push(e);
            else if (!Ht(i, e, t, n, r)) {
                Ft(e, r),
                    e = _t(e, r, null, t);
                try {
                    U(Mt, e)
                } finally {
                    wt(e)
                }
            }
        }
}

function co(e, t) {
    return e = so(e),
        Hi(e, t)
}


function ft(e, t) {
    if (null == t)
        throw Error(a(30));
    return null == e ? t : Array.isArray(e) ? Array.isArray(t) ? (e.push.apply(e, t),
        e) : (e.push(t),
            e) : Array.isArray(t) ? [e].concat(t) : [e, t]
}


function Ft(e, t) {
    switch (e) {
    case "focus":
    case "blur":
        It = null;
        break;
    case "dragenter":
    case "dragleave":
        kt = null;
        break;
    case "mouseover":
    case "mouseout":
        At = null;
        break;
    case "pointerover":
    case "pointerout":
        Dt.delete(t.pointerId);
        break;
    case "gotpointercapture":
    case "lostpointercapture":
        Nt.delete(t.pointerId)
    }
}


function so(e) {
    switch (e) {
        case 99:
            return qi;
        case 98:
            return Ki;
        case 97:
            return Qi;
        case 96:
            return Zi;
        case 95:
            return Xi;
        default:
            throw Error(a(332))
    }
}


function gt(e) {
    if (e) {
        var t = e._dispatchListeners
            , n = e._dispatchInstances;
        if (Array.isArray(t))
            for (var r = 0; r < t.length && !e.isPropagationStopped(); r++)
                y(e, t[r], n[r]);
        else
            t && y(e, t, n);
        e._dispatchListeners = null,
            e._dispatchInstances = null,
            e.isPersistent() || e.constructor.release(e)
    }
}


function Hi(e, t) {
    switch (e) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            break;
        default:
            e = 3
    }
    var n = N;
    N = e;
    try {
        return t()
    } finally {
        N = n
    }
}

function t() {
    var t = to;
    for (; e < t.length; e++) {
        var n = t[e];
        do {
            n = n(!0)
        } while (null !== n)
    }
}

function j(e, t, n, r, i) {
    var o = Js;
    Js |= 4;
    try {
        return co(98, e.bind(null, t, n, r, i))
    } finally {
        0 === (Js = o) && fo()
    }
}

function a(e, t) {
    var n = {};
    for (var r in e)
        Object.prototype.hasOwnProperty.call(e, r) && t.indexOf(r) < 0 && (n[r] = e[r]);
    if (null != e && "function" == typeof Object.getOwnPropertySymbols)
        for (var i = 0, r = Object.getOwnPropertySymbols(e); i < r.length; i++)
            t.indexOf(r[i]) < 0 && Object.prototype.propertyIsEnumerable.call(e, r[i]) && (n[r[i]] = e[r[i]]);
    return n
}

function Kc() {
    if (90 !== yc) {
        var e = 97 < yc ? 97 : yc;
        return yc = 90,
            co(e, Qc)
    }
}


function Gn(e) {
    if (5 === e.tag || 6 === e.tag)
        return e.stateNode;
    throw Error(a(33))
}


function Yn(e) {
    return e[Hn] || null
}


function Ie() {
    /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/facebook/regenerator/blob/main/LICENSE */
    Ie = function t() {
        return e
    }
        ;
    var t, e = {}, r = Object.prototype, n = r.hasOwnProperty, o = Object.defineProperty || function (t, e, r) {
        t[e] = r.value
    }
        , i = "function" == typeof Symbol ? Symbol : {}, a = i.iterator || "@@iterator", c = i.asyncIterator || "@@asyncIterator", u = i.toStringTag || "@@toStringTag";
    function s(t, e, r) {
        return Object.defineProperty(t, e, {
            value: r,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }),
            t[e]
    }
    try {
        s({}, "")
    } catch (t) {
        s = function t(e, r, n) {
            return e[r] = n
        }
    }
    function l(t, e, r, n) {
        var i = e && e.prototype instanceof g ? e : g
            , a = Object.create(i.prototype)
            , c = new S(n || []);
        return o(a, "_invoke", {
            value: I(t, r, c)
        }),
            a
    }
    function f(t, e, r) {
        try {
            return {
                type: "normal",
                arg: t.call(e, r)
            }
        } catch (t) {
            return {
                type: "throw",
                arg: t
            }
        }
    }
    e.wrap = l;
    var d = "suspendedStart"
        , p = "suspendedYield"
        , h = "executing"
        , v = "completed"
        , y = {};
    function g() { }
    function m() { }
    function b() { }
    var w = {};
    s(w, a, (function () {
        return this
    }
    ));
    var A = Object.getPrototypeOf
        , j = A && A(A(k([])));
    j && j !== r && n.call(j, a) && (w = j);
    var E = b.prototype = g.prototype = Object.create(w);
    function O(t) {
        ["next", "throw", "return"].forEach((function (e) {
            s(t, e, (function (t) {
                return this._invoke(e, t)
            }
            ))
        }
        ))
    }
    function x(t, e) {
        function r(o, i, a, c) {
            var u = f(t[o], t, i);
            if ("throw" !== u.type) {
                var s = u.arg
                    , l = s.value;
                return l && "object" == be(l) && n.call(l, "__await") ? e.resolve(l.__await).then((function (t) {
                    r("next", t, a, c)
                }
                ), (function (t) {
                    r("throw", t, a, c)
                }
                )) : e.resolve(l).then((function (t) {
                    s.value = t,
                        a(s)
                }
                ), (function (t) {
                    return r("throw", t, a, c)
                }
                ))
            }
            c(u.arg)
        }
        var i;
        o(this, "_invoke", {
            value: function t(n, o) {
                function a() {
                    return new e((function (t, e) {
                        r(n, o, t, e)
                    }
                    ))
                }
                return i = i ? i.then(a, a) : a()
            }
        })
    }
    function I(e, r, n) {
        var o = d;
        return function (i, a) {
            if (o === h)
                throw Error("Generator is already running");
            if (o === v) {
                if ("throw" === i)
                    throw a;
                return {
                    value: t,
                    done: !0
                }
            }
            for (n.method = i,
                n.arg = a; ;) {
                var c = n.delegate;
                if (c) {
                    var u = M(c, n);
                    if (u) {
                        if (u === y)
                            continue;
                        return u
                    }
                }
                if ("next" === n.method)
                    n.sent = n._sent = n.arg;
                else if ("throw" === n.method) {
                    if (o === d)
                        throw o = v,
                        n.arg;
                    n.dispatchException(n.arg)
                } else
                    "return" === n.method && n.abrupt("return", n.arg);
                o = h;
                var s = f(e, r, n);
                if ("normal" === s.type) {
                    if (o = n.done ? v : p,
                        s.arg === y)
                        continue;
                    return {
                        value: s.arg,
                        done: n.done
                    }
                }
                "throw" === s.type && (o = v,
                    n.method = "throw",
                    n.arg = s.arg)
            }
        }
    }
    function M(e, r) {
        var n = r.method
            , o = e.iterator[n];
        if (o === t)
            return r.delegate = null,
                "throw" === n && e.iterator.return && (r.method = "return",
                    r.arg = t,
                    M(e, r),
                    "throw" === r.method) || "return" !== n && (r.method = "throw",
                        r.arg = new TypeError("The iterator does not provide a '" + n + "' method")),
                y;
        var i = f(o, e.iterator, r.arg);
        if ("throw" === i.type)
            return r.method = "throw",
                r.arg = i.arg,
                r.delegate = null,
                y;
        var a = i.arg;
        return a ? a.done ? (r[e.resultName] = a.value,
            r.next = e.nextLoc,
            "return" !== r.method && (r.method = "next",
                r.arg = t),
            r.delegate = null,
            y) : a : (r.method = "throw",
                r.arg = new TypeError("iterator result is not an object"),
                r.delegate = null,
                y)
    }
    function L(t) {
        var e = {
            tryLoc: t[0]
        };
        1 in t && (e.catchLoc = t[1]),
            2 in t && (e.finallyLoc = t[2],
                e.afterLoc = t[3]),
            this.tryEntries.push(e)
    }
    function N(t) {
        var e = t.completion || {};
        e.type = "normal",
            delete e.arg,
            t.completion = e
    }
    function S(t) {
        this.tryEntries = [{
            tryLoc: "root"
        }],
            t.forEach(L, this),
            this.reset(!0)
    }
    function k(e) {
        if (e || "" === e) {
            var r = e[a];
            if (r)
                return r.call(e);
            if ("function" == typeof e.next)
                return e;
            if (!isNaN(e.length)) {
                var o = -1
                    , i = function r() {
                        for (; ++o < e.length;)
                            if (n.call(e, o))
                                return r.value = e[o],
                                    r.done = !1,
                                    r;
                        return r.value = t,
                            r.done = !0,
                            r
                    };
                return i.next = i
            }
        }
        throw new TypeError(be(e) + " is not iterable")
    }
    return m.prototype = b,
        o(E, "constructor", {
            value: b,
            configurable: !0
        }),
        o(b, "constructor", {
            value: m,
            configurable: !0
        }),
        m.displayName = s(b, u, "GeneratorFunction"),
        e.isGeneratorFunction = function (t) {
            var e = "function" == typeof t && t.constructor;
            return !!e && (e === m || "GeneratorFunction" === (e.displayName || e.name))
        }
        ,
        e.mark = function (t) {
            return Object.setPrototypeOf ? Object.setPrototypeOf(t, b) : (t.__proto__ = b,
                s(t, u, "GeneratorFunction")),
                t.prototype = Object.create(E),
                t
        }
        ,
        e.awrap = function (t) {
            return {
                __await: t
            }
        }
        ,
        O(x.prototype),
        s(x.prototype, c, (function () {
            return this
        }
        )),
        e.AsyncIterator = x,
        e.async = function (t, r, n, o, i) {
            void 0 === i && (i = Promise);
            var a = new x(l(t, r, n, o), i);
            return e.isGeneratorFunction(r) ? a : a.next().then((function (t) {
                return t.done ? t.value : a.next()
            }
            ))
        }
        ,
        O(E),
        s(E, u, "Generator"),
        s(E, a, (function () {
            return this
        }
        )),
        s(E, "toString", (function () {
            return "[object Generator]"
        }
        )),
        e.keys = function (t) {
            var e = Object(t)
                , r = [];
            for (var n in e)
                r.push(n);
            return r.reverse(),
                function t() {
                    for (; r.length;) {
                        var n = r.pop();
                        if (n in e)
                            return t.value = n,
                                t.done = !1,
                                t
                    }
                    return t.done = !0,
                        t
                }
        }
        ,
        e.values = k,
        S.prototype = {
            constructor: S,
            reset: function e(r) {
                if (this.prev = 0,
                    this.next = 0,
                    this.sent = this._sent = t,
                    this.done = !1,
                    this.delegate = null,
                    this.method = "next",
                    this.arg = t,
                    this.tryEntries.forEach(N),
                    !r)
                    for (var o in this)
                        "t" === o.charAt(0) && n.call(this, o) && !isNaN(+o.slice(1)) && (this[o] = t)
            },
            stop: function t() {
                this.done = !0;
                var e = this.tryEntries[0].completion;
                if ("throw" === e.type)
                    throw e.arg;
                return this.rval
            },
            dispatchException: function e(r) {
                if (this.done)
                    throw r;
                var o = this;
                function i(e, n) {
                    return u.type = "throw",
                        u.arg = r,
                        o.next = e,
                        n && (o.method = "next",
                            o.arg = t),
                        !!n
                }
                for (var a = this.tryEntries.length - 1; a >= 0; --a) {
                    var c = this.tryEntries[a]
                        , u = c.completion;
                    if ("root" === c.tryLoc)
                        return i("end");
                    if (c.tryLoc <= this.prev) {
                        var s = n.call(c, "catchLoc")
                            , l = n.call(c, "finallyLoc");
                        if (s && l) {
                            if (this.prev < c.catchLoc)
                                return i(c.catchLoc, !0);
                            if (this.prev < c.finallyLoc)
                                return i(c.finallyLoc)
                        } else if (s) {
                            if (this.prev < c.catchLoc)
                                return i(c.catchLoc, !0)
                        } else {
                            if (!l)
                                throw Error("try statement without catch or finally");
                            if (this.prev < c.finallyLoc)
                                return i(c.finallyLoc)
                        }
                    }
                }
            },
            abrupt: function t(e, r) {
                for (var o = this.tryEntries.length - 1; o >= 0; --o) {
                    var i = this.tryEntries[o];
                    if (i.tryLoc <= this.prev && n.call(i, "finallyLoc") && this.prev < i.finallyLoc) {
                        var a = i;
                        break
                    }
                }
                a && ("break" === e || "continue" === e) && a.tryLoc <= r && r <= a.finallyLoc && (a = null);
                var c = a ? a.completion : {};
                return c.type = e,
                    c.arg = r,
                    a ? (this.method = "next",
                        this.next = a.finallyLoc,
                        y) : this.complete(c)
            },
            complete: function t(e, r) {
                if ("throw" === e.type)
                    throw e.arg;
                return "break" === e.type || "continue" === e.type ? this.next = e.arg : "return" === e.type ? (this.rval = this.arg = e.arg,
                    this.method = "return",
                    this.next = "end") : "normal" === e.type && r && (this.next = r),
                    y
            },
            finish: function t(e) {
                for (var r = this.tryEntries.length - 1; r >= 0; --r) {
                    var n = this.tryEntries[r];
                    if (n.finallyLoc === e)
                        return this.complete(n.completion, n.afterLoc),
                            N(n),
                            y
                }
            },
            catch: function t(e) {
                for (var r = this.tryEntries.length - 1; r >= 0; --r) {
                    var n = this.tryEntries[r];
                    if (n.tryLoc === e) {
                        var o = n.completion;
                        if ("throw" === o.type) {
                            var i = o.arg;
                            N(n)
                        }
                        return i
                    }
                }
                throw Error("illegal catch attempt")
            },
            delegateYield: function e(r, n, o) {
                return this.delegate = {
                    iterator: k(r),
                    resultName: n,
                    nextLoc: o
                },
                    "next" === this.method && (this.arg = t),
                    y
            }
        },
        e
}


function download(e, r, n) {
    var o = n.isCanDirectDownload
        , c = void 0 !== o && o;
    return Object(a.b)(t, void 0, void 0, Ie().mark(
        (function t() {
            var n = this, o, a, u, s, l, f, d, y, g, b, w, A, j, E, O, x, I;
            return Ie().wrap((function t(M) {
                for (; ;)
                    switch (M.prev = M.next) {
                        case 0:
                            if (this.props.isLogin) {
                                M.next = 3;
                                break
                            }
                            return this.handelShowLogin(),
                                M.abrupt("return");
                        case 3:
                            if (w = e.map((function (t) {
                                var e;
                                return n.props.list.filter((function (e) {
                                    return e.fid === t
                                }
                                ))[0]
                            }
                            )),
                                A = Object(m.f)(w),
                                p.b.click("function_download", Object.assign({
                                    c: "function",
                                    d: "download",
                                    is_native: this.props.isPcNewUser ? 1 : 0
                                }, A)),
                                !(e.length <= 0)) {
                                M.next = 9;
                                break
                            }
                            return this.setState({
                                notSelectInfo: {
                                    show: !0,
                                    text: "\u8bf7\u5148\u9009\u62e9\u6587\u4ef6\uff0c\u4e4b\u540e\u624d\u80fd\u8fdb\u884c\u4e0b\u8f7d\u64cd\u4f5c\u54e6~"
                                }
                            }),
                                M.abrupt("return");
                        case 9:
                            if (!this.props.isOwner) {
                                M.next = 15;
                                break
                            }
                            if (!c) {
                                M.next = 13;
                                break
                            }
                            return this.doDownload(e[0]),
                                M.abrupt("return");
                        case 13:
                            return null === (a = null === (o = this.calloutRef) || void 0 === o ? void 0 : o.current) || void 0 === a || a.tryCheckDownloadCallout(w),
                                M.abrupt("return");
                        case 15:
                            return p.b.click("save_to_drive", {
                                c: "function",
                                d: "save"
                            }),
                                j = i.a.loading("\u4fdd\u5b58\u4e2d...", 0),
                                M.next = 19,
                                this.doSave({
                                    fid_list: e,
                                    fid_token_list: r,
                                    isDefaultSave: !this.props.savePathInfo.folderFid
                                });
                        case 19:
                            if (E = M.sent,
                                null === (u = null == E ? void 0 : E.save_as) || void 0 === u ? void 0 : u.save_as_top_fids) {
                                M.next = 24;
                                break
                            }
                            return h.a.Monitor(v.a.shareLandingSave).success({
                                msg: "\u8f6c\u5b58\u4e0b\u8f7d\u5931\u8d25"
                            }),
                                j(),
                                M.abrupt("return");
                        case 24:
                            if (O = E.save_as.save_as_top_fids,
                                !c) {
                                M.next = 29;
                                break
                            }
                            return this.doDownload(O[0]),
                                j(),
                                M.abrupt("return");
                        case 29:
                            j(),
                                x = O.map((function (t) {
                                    return {
                                        fid: t
                                    }
                                }
                                )),
                                I = Object(k.b)(w),
                                (null === (s = window.chrome) || void 0 === s ? void 0 : s.quarkRoutePrivate) ? null === (f = null === (l = this.calloutRef) || void 0 === l ? void 0 : l.current) || void 0 === f || f.tryCheckDownloadCallout(x) : this.props.isPcNewUser ? null === (y = null === (d = this.calloutRef) || void 0 === d ? void 0 : d.current) || void 0 === y || y.noLoginPcDownload({
                                    type: I.downloadType,
                                    data: {
                                        list: x
                                    }
                                }) : null === (b = null === (g = this.calloutRef) || void 0 === g ? void 0 : g.current) || void 0 === b || b.download({
                                    type: I.downloadType,
                                    data: {
                                        list: x
                                    }
                                });
                        case 33:
                        case "end":
                            return M.stop()
                    }
            }
            ), t, this)
        }
        )))
}


function ao() {
    switch (Yi()) {
        case qi:
            return 99;
        case Ki:
            return 98;
        case Qi:
            return 97;
        case Zi:
            return 96;
        case Xi:
            return 95;
        default:
            throw Error(a(332))
    }
}

function Gc(e) {
    var t = ao();
    return co(99, Yc.bind(null, e, t)),
        null
}

function wo() {
    bo = yo = vo = null
}

function Bc() {
    for (; null !== tc;)
        tc = Uc(tc)
}

function Uc(e) {
    var t = xc(e.alternate, e, nc);
    return e.memoizedProps = e.pendingProps,
        null === t && (t = Vc(e)),
        Us.current = null,
        t
}

function Si(e) {
    0 > Oi || (e.current = Ti[Oi],
        Ti[Oi] = null,
        Oi--)
}

function Jo() {
    Si(Ko),
        Si(Qo),
        Si(Zo)
}

function vs(e, t, n) {
    var r = t.pendingProps;
    switch (t.tag) {
        case 2:
        case 16:
        case 15:
        case 0:
        case 11:
        case 7:
        case 8:
        case 12:
        case 9:
        case 14:
            return null;
        case 1:
            return Li(t.type) && ji(),
                null;
        case 3:
            return Jo(),
                Si(Di),
                Si(Ai),
                (n = t.stateNode).pendingContext && (n.context = n.pendingContext,
                    n.pendingContext = null),
                null !== e && null !== e.child || !qa(t) || (t.effectTag |= 4),
                null;
        case 5:
            ta(t),
                n = Xo(Zo.current);
            var o = t.type;
            if (null !== e && null != t.stateNode)
                ls(e, t, o, r, n),
                    e.ref !== t.ref && (t.effectTag |= 128);
            else {
                if (!r) {
                    if (null === t.stateNode)
                        throw Error(a(166));
                    return null
                }
                if (e = Xo(Ko.current),
                    qa(t)) {
                    r = t.stateNode,
                        o = t.type;
                    var s = t.memoizedProps;
                    switch (r[Bn] = t,
                    r[Hn] = s,
                    o) {
                        case "iframe":
                        case "object":
                        case "embed":
                            on("load", r);
                            break;
                        case "video":
                        case "audio":
                            for (e = 0; e < it.length; e++)
                                on(it[e], r);
                            break;
                        case "source":
                            on("error", r);
                            break;
                        case "img":
                        case "image":
                        case "link":
                            on("error", r),
                                on("load", r);
                            break;
                        case "form":
                            on("reset", r),
                                on("submit", r);
                            break;
                        case "details":
                            on("toggle", r);
                            break;
                        case "input":
                            Ie(r, s),
                                on("invalid", r),
                                bn(n, "onChange");
                            break;
                        case "select":
                            r._wrapperState = {
                                wasMultiple: !!s.multiple
                            },
                                on("invalid", r),
                                bn(n, "onChange");
                            break;
                        case "textarea":
                            Re(r, s),
                                on("invalid", r),
                                bn(n, "onChange")
                    }
                    for (var c in mn(o, s),
                        e = null,
                        s)
                        if (s.hasOwnProperty(c)) {
                            var l = s[c];
                            "children" === c ? "string" == typeof l ? r.textContent !== l && (e = ["children", l]) : "number" == typeof l && r.textContent !== "" + l && (e = ["children", "" + l]) : C.hasOwnProperty(c) && null != l && bn(n, c)
                        }
                    switch (o) {
                        case "input":
                            Te(r),
                                De(r, s, !0);
                            break;
                        case "textarea":
                            Te(r),
                                Be(r);
                            break;
                        case "select":
                        case "option":
                            break;
                        default:
                            "function" == typeof s.onClick && (r.onclick = wn)
                    }
                    n = e,
                        t.updateQueue = n,
                        null !== n && (t.effectTag |= 4)
                } else {
                    switch (c = 9 === n.nodeType ? n : n.ownerDocument,
                    e === yn && (e = We(o)),
                    e === yn ? "script" === o ? ((e = c.createElement("div")).innerHTML = "<script><\/script>",
                        e = e.removeChild(e.firstChild)) : "string" == typeof r.is ? e = c.createElement(o, {
                            is: r.is
                        }) : (e = c.createElement(o),
                            "select" === o && (c = e,
                                r.multiple ? c.multiple = !0 : r.size && (c.size = r.size))) : e = c.createElementNS(e, o),
                    e[Bn] = t,
                    e[Hn] = r,
                    ss(e, t, !1, !1),
                    t.stateNode = e,
                    c = vn(o, r),
                    o) {
                        case "iframe":
                        case "object":
                        case "embed":
                            on("load", e),
                                l = r;
                            break;
                        case "video":
                        case "audio":
                            for (l = 0; l < it.length; l++)
                                on(it[l], e);
                            l = r;
                            break;
                        case "source":
                            on("error", e),
                                l = r;
                            break;
                        case "img":
                        case "image":
                        case "link":
                            on("error", e),
                                on("load", e),
                                l = r;
                            break;
                        case "form":
                            on("reset", e),
                                on("submit", e),
                                l = r;
                            break;
                        case "details":
                            on("toggle", e),
                                l = r;
                            break;
                        case "input":
                            Ie(e, r),
                                l = Se(e, r),
                                on("invalid", e),
                                bn(n, "onChange");
                            break;
                        case "option":
                            l = Le(e, r);
                            break;
                        case "select":
                            e._wrapperState = {
                                wasMultiple: !!r.multiple
                            },
                                l = i({}, r, {
                                    value: void 0
                                }),
                                on("invalid", e),
                                bn(n, "onChange");
                            break;
                        case "textarea":
                            Re(e, r),
                                l = ze(e, r),
                                on("invalid", e),
                                bn(n, "onChange");
                            break;
                        default:
                            l = r
                    }
                    mn(o, l);
                    var u = l;
                    for (s in u)
                        if (u.hasOwnProperty(s)) {
                            var d = u[s];
                            "style" === s ? pn(e, d) : "dangerouslySetInnerHTML" === s ? null != (d = d ? d.__html : void 0) && qe(e, d) : "children" === s ? "string" == typeof d ? ("textarea" !== o || "" !== d) && Ke(e, d) : "number" == typeof d && Ke(e, "" + d) : "suppressContentEditableWarning" !== s && "suppressHydrationWarning" !== s && "autoFocus" !== s && (C.hasOwnProperty(s) ? null != d && bn(n, s) : null != d && te(e, s, d, c))
                        }
                    switch (o) {
                        case "input":
                            Te(e),
                                De(e, r, !1);
                            break;
                        case "textarea":
                            Te(e),
                                Be(e);
                            break;
                        case "option":
                            null != r.value && e.setAttribute("value", "" + xe(r.value));
                            break;
                        case "select":
                            e.multiple = !!r.multiple,
                                null != (n = r.value) ? je(e, !!r.multiple, n, !1) : null != r.defaultValue && je(e, !!r.multiple, r.defaultValue, !0);
                            break;
                        default:
                            "function" == typeof l.onClick && (e.onclick = wn)
                    }
                    Nn(o, r) && (t.effectTag |= 4)
                }
                null !== t.ref && (t.effectTag |= 128)
            }
            return null;
        case 6:
            if (e && null != t.stateNode)
                us(e, t, e.memoizedProps, r);
            else {
                if ("string" != typeof r && null === t.stateNode)
                    throw Error(a(166));
                n = Xo(Zo.current),
                    Xo(Ko.current),
                    qa(t) ? (n = t.stateNode,
                        r = t.memoizedProps,
                        n[Bn] = t,
                        n.nodeValue !== r && (t.effectTag |= 4)) : ((n = (9 === n.nodeType ? n : n.ownerDocument).createTextNode(r))[Bn] = t,
                            t.stateNode = n)
            }
            return null;
        case 13:
            return Si(na),
                r = t.memoizedState,
                0 != (64 & t.effectTag) ? (t.expirationTime = n,
                    t) : (n = null !== r,
                        r = !1,
                        null === e ? void 0 !== t.memoizedProps.fallback && qa(t) : (r = null !== (o = e.memoizedState),
                            n || null === o || null !== (o = e.child.sibling) && (null !== (s = t.firstEffect) ? (t.firstEffect = o,
                                o.nextEffect = s) : (t.firstEffect = t.lastEffect = o,
                                    o.nextEffect = null),
                                o.effectTag = 8)),
                        n && !r && 0 != (2 & t.mode) && (null === e && !0 !== t.memoizedProps.unstable_avoidThisFallback || 0 != (1 & na.current) ? rc === qs && (rc = Zs) : (rc !== qs && rc !== Zs || (rc = Xs),
                            0 !== cc && null !== ec && (pl(ec, nc),
                                gl(ec, cc)))),
                        (n || r) && (t.effectTag |= 4),
                        null);
        case 4:
            return Jo(),
                null;
        case 10:
            return _o(t),
                null;
        case 17:
            return Li(t.type) && ji(),
                null;
        case 19:
            if (Si(na),
                null === (r = t.memoizedState))
                return null;
            if (o = 0 != (64 & t.effectTag),
                null === (s = r.rendering)) {
                if (o)
                    ms(r, !1);
                else if (rc !== qs || null !== e && 0 != (64 & e.effectTag))
                    for (s = t.child; null !== s;) {
                        if (null !== (e = ra(s))) {
                            for (t.effectTag |= 64,
                                ms(r, !1),
                                null !== (o = e.updateQueue) && (t.updateQueue = o,
                                    t.effectTag |= 4),
                                null === r.lastEffect && (t.firstEffect = null),
                                t.lastEffect = r.lastEffect,
                                r = t.child; null !== r;)
                                s = n,
                                    (o = r).effectTag &= 2,
                                    o.nextEffect = null,
                                    o.firstEffect = null,
                                    o.lastEffect = null,
                                    null === (e = o.alternate) ? (o.childExpirationTime = 0,
                                        o.expirationTime = s,
                                        o.child = null,
                                        o.memoizedProps = null,
                                        o.memoizedState = null,
                                        o.updateQueue = null,
                                        o.dependencies = null) : (o.childExpirationTime = e.childExpirationTime,
                                            o.expirationTime = e.expirationTime,
                                            o.child = e.child,
                                            o.memoizedProps = e.memoizedProps,
                                            o.memoizedState = e.memoizedState,
                                            o.updateQueue = e.updateQueue,
                                            s = e.dependencies,
                                            o.dependencies = null === s ? null : {
                                                expirationTime: s.expirationTime,
                                                firstContext: s.firstContext,
                                                responders: s.responders
                                            }),
                                    r = r.sibling;
                            return Ii(na, 1 & na.current | 2),
                                t.child
                        }
                        s = s.sibling
                    }
            } else {
                if (!o)
                    if (null !== (e = ra(s))) {
                        if (t.effectTag |= 64,
                            o = !0,
                            null !== (n = e.updateQueue) && (t.updateQueue = n,
                                t.effectTag |= 4),
                            ms(r, !0),
                            null === r.tail && "hidden" === r.tailMode && !s.alternate)
                            return null !== (t = t.lastEffect = r.lastEffect) && (t.nextEffect = null),
                                null
                    } else
                        2 * oo() - r.renderingStartTime > r.tailExpiration && 1 < n && (t.effectTag |= 64,
                            o = !0,
                            ms(r, !1),
                            t.expirationTime = t.childExpirationTime = n - 1);
                r.isBackwards ? (s.sibling = t.child,
                    t.child = s) : (null !== (n = r.last) ? n.sibling = s : t.child = s,
                        r.last = s)
            }
            return null !== r.tail ? (0 === r.tailExpiration && (r.tailExpiration = oo() + 500),
                n = r.tail,
                r.rendering = n,
                r.tail = n.sibling,
                r.lastEffect = t.lastEffect,
                r.renderingStartTime = oo(),
                n.sibling = null,
                t = na.current,
                Ii(na, o ? 1 & t | 2 : 1 & t),
                n) : null
    }
    throw Error(a(156, t.tag))
}


function Vc(e) {
    tc = e;
    do {
        var t = tc.alternate;
        if (e = tc.return,
            0 == (2048 & tc.effectTag)) {
            if (t = vs(t, tc, nc),
                1 === nc || 1 !== tc.childExpirationTime) {
                for (var n = 0, r = tc.child; null !== r;) {
                    var i = r.expirationTime
                        , o = r.childExpirationTime;
                    i > n && (n = i),
                        o > n && (n = o),
                        r = r.sibling
                }
                tc.childExpirationTime = n
            }
            if (null !== t)
                return t;
            null !== e && 0 == (2048 & e.effectTag) && (null === e.firstEffect && (e.firstEffect = tc.firstEffect),
                null !== tc.lastEffect && (null !== e.lastEffect && (e.lastEffect.nextEffect = tc.firstEffect),
                    e.lastEffect = tc.lastEffect),
                1 < tc.effectTag && (null !== e.lastEffect ? e.lastEffect.nextEffect = tc : e.firstEffect = tc,
                    e.lastEffect = tc))
        } else {
            if (null !== (t = ys(tc)))
                return t.effectTag &= 2047,
                    t;
            null !== e && (e.firstEffect = e.lastEffect = null,
                e.effectTag |= 2048)
        }
        if (null !== (t = tc.sibling))
            return t;
        tc = e
    } while (null !== tc);
    return rc === qs && (rc = 5),
        null
}



function Uc(e) {
    var t = xc(e.alternate, e, nc);
    return e.memoizedProps = e.pendingProps,
        null === t && (t = Vc(e)),
        Us.current = null,
        t
}

function gs(e, t, n) {
    null !== e && (t.dependencies = e.dependencies);
    var r = t.expirationTime;
    if (0 !== r && Fc(r),
        t.childExpirationTime < n)
        return null;
    if (null !== e && t.child !== e.child)
        throw Error(a(153));
    if (null !== t.child) {
        for (n = sl(e = t.child, e.pendingProps),
            t.child = n,
            n.return = t; null !== e.sibling;)
            e = e.sibling,
                (n = n.sibling = sl(e, e.pendingProps)).return = t;
        n.sibling = null
    }
    return t.child
}


function Ka() {
    Ha = Ba = null,
        Ua = !1
}

function Si(e) {
    0 > Oi || (e.current = Ti[Oi],
        Ti[Oi] = null,
        Oi--)
}

function We(e) {
    switch (e) {
        case "svg":
            return "http://www.w3.org/2000/svg";
        case "math":
            return "http://www.w3.org/1998/Math/MathML";
        default:
            return "http://www.w3.org/1999/xhtml"
    }
}


function Ge(e, t) {
    return null == e || "http://www.w3.org/1999/xhtml" === e ? We(t) : "http://www.w3.org/2000/svg" === e && "foreignObject" === t ? "http://www.w3.org/1999/xhtml" : e
}

function $o(e, t) {
    switch (Ii(Zo, t),
    Ii(Qo, e),
    Ii(Ko, qo),
    e = t.nodeType) {
        case 9:
        case 11:
            t = (t = t.documentElement) ? t.namespaceURI : Ge(null, "");
            break;
        default:
            t = Ge(t = (e = 8 === e ? t.parentNode : t).namespaceURI || null, e = e.tagName)
    }
    Si(Ko),
        Ii(Ko, t)
}


function os(e) {
    var t = e.stateNode;
    t.pendingContext ? zi(e, t.pendingContext, t.pendingContext !== t.context) : t.context && zi(e, t.context, !1),
        $o(e, t.containerInfo)
}


function Ii(e, t) {
    Oi++,
        Ti[Oi] = e.current,
        e.current = t
}

function zi(e, t, n) {
    if (Ai.current !== ki)
        throw Error(a(168));
    Ii(Ai, t),
        Ii(Di, n)
}

xc = function (e, t, n) {
    var r = t.expirationTime;
    if (null !== e) {
        var i = t.pendingProps;
        if (e.memoizedProps !== i || Di.current)
            Za = !0;
        else {
            if (r < n) {
                switch (Za = !1,
                t.tag) {
                    case 3:
                        os(t),
                            Ka();
                        break;
                    case 5:
                        if (ea(t),
                            4 & t.mode && 1 !== n && i.hidden)
                            return t.expirationTime = t.childExpirationTime = 1,
                                null;
                        break;
                    case 1:
                        Li(t.type) && Fi(t);
                        break;
                    case 4:
                        $o(t, t.stateNode.containerInfo);
                        break;
                    case 10:
                        r = t.memoizedProps.value,
                            i = t.type._context,
                            Ii(mo, i._currentValue),
                            i._currentValue = r;
                        break;
                    case 13:
                        if (null !== t.memoizedState)
                            return 0 !== (r = t.child.childExpirationTime) && r >= n ? ds(e, t, n) : (Ii(na, 1 & na.current),
                                null !== (t = gs(e, t, n)) ? t.sibling : null);
                        Ii(na, 1 & na.current);
                        break;
                    case 19:
                        if (r = t.childExpirationTime >= n,
                            0 != (64 & e.effectTag)) {
                            if (r)
                                return ps(e, t, n);
                            t.effectTag |= 64
                        }
                        if (null !== (i = t.memoizedState) && (i.rendering = null,
                            i.tail = null),
                            Ii(na, na.current),
                            !r)
                            return null
                }
                return gs(e, t, n)
            }
            Za = !1
        }
    } else
        Za = !1;
    switch (t.expirationTime = 0,
    t.tag) {
        case 2:
            if (r = t.type,
                null !== e && (e.alternate = null,
                    t.alternate = null,
                    t.effectTag |= 2),
                e = t.pendingProps,
                i = Pi(t, Ai.current),
                xo(t, n),
                i = pa(null, t, r, e, i, n),
                t.effectTag |= 1,
                "object" == typeof i && null !== i && "function" == typeof i.render && void 0 === i.$$typeof) {
                if (t.tag = 1,
                    t.memoizedState = null,
                    t.updateQueue = null,
                    Li(r)) {
                    var o = !0;
                    Fi(t)
                } else
                    o = !1;
                t.memoizedState = null !== i.state && void 0 !== i.state ? i.state : null,
                    To(t);
                var s = r.getDerivedStateFromProps;
                "function" == typeof s && Lo(t, r, s, e),
                    i.updater = jo,
                    t.stateNode = i,
                    i._reactInternalFiber = t,
                    Bo(t, r, e, n),
                    t = is(null, t, r, !0, o, n)
            } else
                t.tag = 0,
                    Xa(null, t, i, n),
                    t = t.child;
            return t;
        case 16:
            e: {
                if (i = t.elementType,
                    null !== e && (e.alternate = null,
                        t.alternate = null,
                        t.effectTag |= 2),
                    e = t.pendingProps,
                    we(i),
                    1 !== i._status)
                    throw i._result;
                switch (i = i._result,
                t.type = i,
                o = t.tag = al(i),
                e = go(i, e),
                o) {
                    case 0:
                        t = ns(null, t, i, e, n);
                        break e;
                    case 1:
                        t = rs(null, t, i, e, n);
                        break e;
                    case 11:
                        t = $a(null, t, i, e, n);
                        break e;
                    case 14:
                        t = Ja(null, t, i, go(i.type, e), r, n);
                        break e
                }
                throw Error(a(306, i, ""))
            }
            return t;
        case 0:
            return r = t.type,
                i = t.pendingProps,
                ns(e, t, r, i = t.elementType === r ? i : go(r, i), n);
        case 1:
            return r = t.type,
                i = t.pendingProps,
                rs(e, t, r, i = t.elementType === r ? i : go(r, i), n);
        case 3:
            if (os(t),
                r = t.updateQueue,
                null === e || null === r)
                throw Error(a(282));
            if (r = t.pendingProps,
                i = null !== (i = t.memoizedState) ? i.element : null,
                Oo(e, t),
                Ao(t, r, null, n),
                (r = t.memoizedState.element) === i)
                Ka(),
                    t = gs(e, t, n);
            else {
                if ((i = t.stateNode.hydrate) && (Ha = zn(t.stateNode.containerInfo.firstChild),
                    Ba = t,
                    i = Ua = !0),
                    i)
                    for (n = Yo(t, null, r, n),
                        t.child = n; n;)
                        n.effectTag = -3 & n.effectTag | 1024,
                            n = n.sibling;
                else
                    Xa(e, t, r, n),
                        Ka();
                t = t.child
            }
            return t;
        case 5:
            return ea(t),
                null === e && Ga(t),
                r = t.type,
                i = t.pendingProps,
                o = null !== e ? e.memoizedProps : null,
                s = i.children,
                Pn(r, i) ? s = null : null !== o && Pn(r, o) && (t.effectTag |= 16),
                ts(e, t),
                4 & t.mode && 1 !== n && i.hidden ? (t.expirationTime = t.childExpirationTime = 1,
                    t = null) : (Xa(e, t, s, n),
                        t = t.child),
                t;
        case 6:
            return null === e && Ga(t),
                null;
        case 13:
            return ds(e, t, n);
        case 4:
            return $o(t, t.stateNode.containerInfo),
                r = t.pendingProps,
                null === e ? t.child = Go(t, null, r, n) : Xa(e, t, r, n),
                t.child;
        case 11:
            return r = t.type,
                i = t.pendingProps,
                $a(e, t, r, i = t.elementType === r ? i : go(r, i), n);
        case 7:
            return Xa(e, t, t.pendingProps, n),
                t.child;
        case 8:
        case 12:
            return Xa(e, t, t.pendingProps.children, n),
                t.child;
        case 10:
            e: {
                r = t.type._context,
                    i = t.pendingProps,
                    s = t.memoizedProps,
                    o = i.value;
                var c = t.type._context;
                if (Ii(mo, c._currentValue),
                    c._currentValue = o,
                    null !== s)
                    if (c = s.value,
                        0 === (o = ni(c, o) ? 0 : 0 | ("function" == typeof r._calculateChangedBits ? r._calculateChangedBits(c, o) : 1073741823))) {
                        if (s.children === i.children && !Di.current) {
                            t = gs(e, t, n);
                            break e
                        }
                    } else
                        for (null !== (c = t.child) && (c.return = t); null !== c;) {
                            var l = c.dependencies;
                            if (null !== l) {
                                s = c.child;
                                for (var u = l.firstContext; null !== u;) {
                                    if (u.context === r && 0 != (u.observedBits & o)) {
                                        1 === c.tag && ((u = So(n, null)).tag = 2,
                                            Io(c, u)),
                                            c.expirationTime < n && (c.expirationTime = n),
                                            null !== (u = c.alternate) && u.expirationTime < n && (u.expirationTime = n),
                                            Mo(c.return, n),
                                            l.expirationTime < n && (l.expirationTime = n);
                                        break
                                    }
                                    u = u.next
                                }
                            } else
                                s = 10 === c.tag && c.type === t.type ? null : c.child;
                            if (null !== s)
                                s.return = c;
                            else
                                for (s = c; null !== s;) {
                                    if (s === t) {
                                        s = null;
                                        break
                                    }
                                    if (null !== (c = s.sibling)) {
                                        c.return = s.return,
                                            s = c;
                                        break
                                    }
                                    s = s.return
                                }
                            c = s
                        }
                Xa(e, t, i.children, n),
                    t = t.child
            }
            return t;
        case 9:
            return i = t.type,
                r = (o = t.pendingProps).children,
                xo(t, n),
                r = r(i = Eo(i, o.unstable_observedBits)),
                t.effectTag |= 1,
                Xa(e, t, r, n),
                t.child;
        case 14:
            return o = go(i = t.type, t.pendingProps),
                Ja(e, t, i, o = go(i.type, o), r, n);
        case 15:
            return es(e, t, t.type, t.pendingProps, r, n);
        case 17:
            return r = t.type,
                i = t.pendingProps,
                i = t.elementType === r ? i : go(r, i),
                null !== e && (e.alternate = null,
                    t.alternate = null,
                    t.effectTag |= 2),
                t.tag = 1,
                Li(r) ? (e = !0,
                    Fi(t)) : e = !1,
                xo(t, n),
                Ro(t, r, i),
                Bo(t, r, i, n),
                is(null, t, r, !0, e, n);
        case 19:
            return ps(e, t, n)
    }
    throw Error(a(156, t.tag))
}


function ln(e, t, n, r) {
    if (rn)
        if (0 < St.length && -1 < Lt.indexOf(e))
            e = Rt(null, e, t, n, r),
            St.push(e);
        else {
            var i = un(e, t, n, r);
            if (null === i)
                Ft(e, r);
            else if (-1 < Lt.indexOf(e))
                e = Rt(i, e, t, n, r),
                St.push(e);
            else if (!Ht(i, e, t, n, r)) {
                Ft(e, r),
                e = _t(e, r, null, t);
                try {
                    U(Mt, e)
                } finally {
                    wt(e)
                }
            }
        }
}

function Uc(e) {
    var t = xc(e.alternate, e, nc);
    return e.memoizedProps = e.pendingProps,
        null === t && (t = Vc(e)),
        Us.current = null,
        t
}

function Kn(e, t) {
    var n = e.stateNode;
    if (!n)
        return null;
    var r = g(n);
    if (!r)
        return null;
    n = r[t];
    e: switch (t) {
        case "onClick":
        case "onClickCapture":
        case "onDoubleClick":
        case "onDoubleClickCapture":
        case "onMouseDown":
        case "onMouseDownCapture":
        case "onMouseMove":
        case "onMouseMoveCapture":
        case "onMouseUp":
        case "onMouseUpCapture":
        case "onMouseEnter":
            (r = !r.disabled) || (r = !("button" === (e = e.type) || "input" === e || "select" === e || "textarea" === e)),
                e = !r;
            break e;
        default:
            e = !1
    }
    if (e)
        return null;
    if (n && "function" != typeof n)
        throw Error(a(231, t, typeof n));
    return n
}


function Qn(e, t, n) {
    (t = Kn(e, n.dispatchConfig.phasedRegistrationNames[t])) && (n._dispatchListeners = ft(n._dispatchListeners, t),
        n._dispatchInstances = ft(n._dispatchInstances, e))
}


function qn(e) {
    do {
        e = e.return
    } while (e && 5 !== e.tag);
    return e || null
}


function Zn(e) {
    if (e && e.dispatchConfig.phasedRegistrationNames) {
        for (var t = e._targetInst, n = []; t;)
            n.push(t),
                t = qn(t);
        for (t = n.length; 0 < t--;)
            Qn(n[t], "captured", e);
        for (t = 0; t < n.length; t++)
            Qn(n[t], "bubbled", e)
    }
}

function Bc() {
    for (; null !== tc;)
        tc = Uc(tc)
}


function zc() {
    var e = Hs.current;
    return Hs.current = ja,
        null === e ? ja : e
}

function sl(e, t) {
    var n = e.alternate;
    return null === n ? ((n = il(e.tag, t, e.key, e.mode)).elementType = e.elementType,
        n.type = e.type,
        n.stateNode = e.stateNode,
        n.alternate = e,
        e.alternate = n) : (n.pendingProps = t,
            n.effectTag = 0,
            n.nextEffect = null,
            n.firstEffect = null,
            n.lastEffect = null),
        n.childExpirationTime = e.childExpirationTime,
        n.expirationTime = e.expirationTime,
        n.child = e.child,
        n.memoizedProps = e.memoizedProps,
        n.memoizedState = e.memoizedState,
        n.updateQueue = e.updateQueue,
        t = e.dependencies,
        n.dependencies = null === t ? null : {
            expirationTime: t.expirationTime,
            firstContext: t.firstContext,
            responders: t.responders
        },
        n.sibling = e.sibling,
        n.index = e.index,
        n.ref = e.ref,
        n
}

function Lc(e, t) {
    e.finishedWork = null,
        e.finishedExpirationTime = 0;
    var n = e.timeoutHandle;
    if (-1 !== n && (e.timeoutHandle = -1,
        jn(n)),
        null !== tc)
        for (n = tc.return; null !== n;) {
            var r = n;
            switch (r.tag) {
                case 1:
                    null != (r = r.type.childContextTypes) && ji();
                    break;
                case 3:
                    Jo(),
                        Si(Di),
                        Si(Ai);
                    break;
                case 5:
                    ta(r);
                    break;
                case 4:
                    Jo();
                    break;
                case 13:
                case 19:
                    Si(na);
                    break;
                case 10:
                    _o(r)
            }
            n = n.return
        }
    ec = e,
        tc = sl(e.current, null),
        nc = t,
        rc = qs,
        ic = null,
        ac = oc = 1073741823,
        sc = null,
        cc = 0,
        lc = !1
}

function ho() {
    if (!ro && null !== to) {
        ro = !0;
        var e = 0;
        try {
            var t = to;
            co(99, (function () {
                for (; e < t.length; e++) {
                    var n = t[e];
                    do {
                        n = n(!0)
                    } while (null !== n)
                }
            }
            )),
                to = null
        } catch (t) {
            throw null !== to && (to = to.slice(e + 1)),
            Ui(qi, fo),
            t
        } finally {
            ro = !1
        }
    }
}


function fo() {
    if (null !== no) {
        var e = no;
        no = null,
            Vi(e)
    }
    ho()
}


function ml(e, t) {
    var n = e.lastExpiredTime;
    (0 === n || n > t) && (e.lastExpiredTime = t)
}

function Dc() {
    if (null !== bc) {
        var e = bc;
        bc = null,
            e.forEach((function (e, t) {
                ml(t, e),
                    Ic(t)
            }
            )),
            fo()
    }
}

z = function () {
    0 == (49 & Js) && (Dc(),
        Kc())
}


function sn(e, t, n, r) {
    F=false
    F || z();
    var i = ln
        , o = F;
    F = !0;
    try {
        j(i, e, t, n, r)
    } finally {
        (F = o) || H()
    }
}

function main() {
    e = 'click'
    t = 1
    Js=0
    bc=null
    yc=90
    result = sn(e, t)
    console.log(result)
}

main()

