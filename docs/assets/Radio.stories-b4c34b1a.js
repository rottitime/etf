import{b as d,d as p,i as c}from"./utils-f016dfc5.js";const l={title:"Components/Form/Radio",tags:["autodocs"],render:({legend:a,radioList:s,...i})=>d(p(s.map(n=>c({...i,name:"radio-example",text:n})),{}),a),argTypes:{legend:{control:"text"},large:{control:"boolean"},onkeyup:{action:"changed",table:{disable:!0}}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=32-159&t=s7R0duWzGfG8Vf2S-0"}}},e={args:{legend:"Pick a option",radioList:[...Array(5).keys()].map(a=>`Option ${a}`)}};var o,r,t;e.parameters={...e.parameters,docs:{...(o=e.parameters)==null?void 0:o.docs,source:{originalSource:`{
  args: {
    legend: 'Pick a option',
    radioList: [...Array(5).keys()].map(i => \`Option \${i}\`)
  }
}`,...(t=(r=e.parameters)==null?void 0:r.docs)==null?void 0:t.source}}};const g=["Default"];export{e as Default,g as __namedExportsOrder,l as default};
//# sourceMappingURL=Radio.stories-b4c34b1a.js.map
