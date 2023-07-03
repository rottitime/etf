import{r as g,M as h}from"./index-a2d68020.js";import{u as c}from"./index-3b846850.js";import"./iframe-bd6a88bf.js";import"../sb-preview/runtime.js";import"./_commonjsHelpers-725317a4.js";import"./index-d475d2ea.js";import"./index-d37d4223.js";import"./index-d38538b0.js";import"./index-356e4a49.js";var p={exports:{}},n={};/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */var x=g,j=Symbol.for("react.element"),u=Symbol.for("react.fragment"),f=Object.prototype.hasOwnProperty,k=x.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner,b={key:!0,ref:!0,__self:!0,__source:!0};function m(t,s,a){var r,i={},o=null,l=null;a!==void 0&&(o=""+a),s.key!==void 0&&(o=""+s.key),s.ref!==void 0&&(l=s.ref);for(r in s)f.call(s,r)&&!b.hasOwnProperty(r)&&(i[r]=s[r]);if(t&&t.defaultProps)for(r in s=t.defaultProps,s)i[r]===void 0&&(i[r]=s[r]);return{$$typeof:j,type:t,key:o,ref:l,props:i,_owner:k.current}}n.Fragment=u;n.jsx=m;n.jsxs=m;p.exports=n;var e=p.exports;function d(t){const s=Object.assign({h1:"h1",p:"p",strong:"strong",code:"code",a:"a"},c(),t.components);return e.jsxs(e.Fragment,{children:[e.jsx(h,{title:"Introduction"}),`
`,e.jsx("style",{children:`

    .main-logo {
      height:100px; 
    }

    .subheading {
      --mediumdark: '#999999';
      font-weight: 700;
      font-size: 13px;
      color: #999;
      letter-spacing: 6px;
      line-height: 24px;
      text-transform: uppercase;
      margin-bottom: 12px;
      margin-top: 40px;
    }

    .link-list {
      display: grid;
      grid-template-columns: 1fr;
      grid-template-rows: 1fr 1fr;
      row-gap: 10px;
    }

    @media (min-width: 620px) {
      .link-list {
        row-gap: 20px;
        column-gap: 20px;
        grid-template-columns: 1fr 1fr;
      }
    }

    @media all and (-ms-high-contrast:none) {
    .link-list {
        display: -ms-grid;
        -ms-grid-columns: 1fr 1fr;
        -ms-grid-rows: 1fr 1fr;
      }
    }

    .link-item {
      display: block;
      padding: 20px;
      border: 1px solid #00000010;
      border-radius: 5px;
      transition: background 150ms ease-out, border 150ms ease-out, transform 150ms ease-out;
      color: #333333;
      display: flex;
      align-items: flex-start;
    }

    .link-item:hover {
      border-color: #1EA7FD50;
      transform: translate3d(0, -3px, 0);
      box-shadow: rgba(0, 0, 0, 0.08) 0 3px 10px 0;
    }

    .link-item:active {
      border-color: #1EA7FD;
      transform: translate3d(0, 0, 0);
    }

    .link-item strong {
      font-weight: 700;
      display: block;
      margin-bottom: 2px;
    }

    .link-item img {
      height: 40px;
      width: 40px;
      margin-right: 15px;
      flex: none;
    }

    .link-item span,
    .link-item p {
      margin: 0;
      font-size: 14px;
      line-height: 20px;
    }

    .tip {
      display: inline-block;
      border-radius: 1em;
      font-size: 11px;
      line-height: 12px;
      font-weight: 700;
      background: #E7FDD8;
      color: #66BF3C;
      padding: 4px 12px;
      margin-right: 10px;
      vertical-align: top;
    }

    .tip-wrapper {
      font-size: 13px;
      line-height: 20px;
      margin-top: 40px;
      margin-bottom: 40px;
    }

    .tip-wrapper code {
      font-size: 12px;
      display: inline-block;
    }
  `}),`
`,e.jsx("img",{src:"images/i-dot-ai.svg",alt:"i.AI logo",class:"main-logo"}),`
`,e.jsx(s.h1,{id:"welcome-to-evaluation-registry-design-system",children:"Welcome to Evaluation Registry design system"}),`
`,e.jsx(s.p,{children:"Use this design system to make services consistent with the i.AI design system. Learn from the research and experience of other service teams and avoid repeating work that's already been done."}),`
`,e.jsxs(s.p,{children:[`This documentation helps you understand the UI components in isolation from your app's business logic, data, and context.
That makes it easy to develop hard-to-reach states. Save these UI states as `,e.jsx(s.strong,{children:"stories"})," to revisit during development, testing, or QA."]}),`
`,e.jsxs(s.p,{children:[`Browse example stories now by navigating to them in the sidebar.
View their code in the `,e.jsx(s.code,{children:"stories"}),` directory to learn how they work.
The UIs built with a `,e.jsx(s.a,{href:"https://componentdriven.org",target:"_blank",rel:"nofollow noopener noreferrer",children:e.jsx(s.strong,{children:"component-driven"})})," process starting with atomic components and ending with pages."]}),`
`,e.jsx("div",{className:"subheading",children:"Configure"}),`
`,e.jsxs("div",{className:"link-list",children:[e.jsxs("a",{className:"link-item",href:"https://storybook.js.org/docs/react/addons/addon-types",target:"_blank",children:[e.jsx("img",{src:"images/plugin.svg",alt:"plugin"}),e.jsx("span",{children:e.jsxs(s.p,{children:[e.jsx("strong",{children:"Presets for popular tools"}),`
Easy setup for TypeScript, SCSS and more.`]})})]}),e.jsxs("a",{className:"link-item",href:"https://storybook.js.org/docs/react/configure/webpack",target:"_blank",children:[e.jsx("img",{src:"images/stackalt.svg",alt:"Build"}),e.jsx("span",{children:e.jsxs(s.p,{children:[e.jsx("strong",{children:"Build configuration"}),`
How to customize webpack and Babel`]})})]}),e.jsxs("a",{className:"link-item",href:"https://storybook.js.org/docs/react/configure/styling-and-css",target:"_blank",children:[e.jsx("img",{src:"images/colors.svg",alt:"colors"}),e.jsx("span",{children:e.jsxs(s.p,{children:[e.jsx("strong",{children:"Styling"}),`
How to load and configure CSS libraries`]})})]}),e.jsxs("a",{className:"link-item",href:"https://storybook.js.org/docs/react/get-started/setup#configure-storybook-for-your-stack",target:"_blank",children:[e.jsx("img",{src:"images/flow.svg",alt:"flow"}),e.jsx("span",{children:e.jsxs(s.p,{children:[e.jsx("strong",{children:"Data"}),`
Providers and mocking for data libraries`]})})]})]}),`
`,e.jsx("div",{className:"subheading",children:"Learn"}),`
`,e.jsxs("div",{className:"link-list",children:[e.jsxs("a",{className:"link-item",href:"https://storybook.js.org/docs",target:"_blank",children:[e.jsx("img",{src:"images/repo.svg",alt:"repo"}),e.jsx("span",{children:e.jsxs(s.p,{children:[e.jsx("strong",{children:"Storybook documentation"}),`
Configure, customize, and extend`]})})]}),e.jsxs("a",{className:"link-item",href:"https://storybook.js.org/tutorials/",target:"_blank",children:[e.jsx("img",{src:"images/direction.svg",alt:"direction"}),e.jsx("span",{children:e.jsxs(s.p,{children:[e.jsx("strong",{children:"In-depth guides"}),`
Best practices from leading teams`]})})]}),e.jsxs("a",{className:"link-item",href:"https://github.com/i-dot-ai/etf",target:"_blank",children:[e.jsx("img",{src:"images/code-brackets.svg",alt:"code"}),e.jsx("span",{children:e.jsxs(s.p,{children:[e.jsx("strong",{children:"GitHub project"}),`
View the source and add issues`]})})]}),e.jsxs("a",{className:"link-item",href:"https://github.com/i-dot-ai/etf/discussions/landing",target:"_blank",children:[e.jsx("img",{src:"images/comments.svg",alt:"comments"}),e.jsx("span",{children:e.jsxs(s.p,{children:[e.jsx("strong",{children:"Discussions"}),`
Chat with maintainers and the community`]})})]})]}),`
`,e.jsx("div",{className:"tip-wrapper",children:e.jsxs(s.p,{children:[e.jsx("span",{className:"tip",children:"Tip"}),"Edit the Markdown in"," ",`
`,e.jsx("code",{children:"stories/Introduction.stories.mdx"})]})})]})}function I(t={}){const{wrapper:s}=Object.assign({},c(),t.components);return s?e.jsx(s,Object.assign({},t,{children:e.jsx(d,t)})):d(t)}export{I as default};
//# sourceMappingURL=Introduction-1b83a5af.js.map
