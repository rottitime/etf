const p={title:"Components/Link",tags:["autodocs"],render:({text:i,external:l})=>`<a href="#" class="txt-link"${l?' rel="external"':""}>${i}</a>`,argTypes:{text:{control:"text"},external:{control:"boolean"}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-273&t=FJwPXpig0RTCQXW7-0"},docs:{description:{component:"A link to another page."}}}},e={args:{text:"My link"}},r={args:{...e.args,external:!0}};var t,a,n;e.parameters={...e.parameters,docs:{...(t=e.parameters)==null?void 0:t.docs,source:{originalSource:`{
  args: {
    text: 'My link'
  }
}`,...(n=(a=e.parameters)==null?void 0:a.docs)==null?void 0:n.source}}};var s,o,c;r.parameters={...r.parameters,docs:{...(s=r.parameters)==null?void 0:s.docs,source:{originalSource:`{
  args: {
    ...Link.args,
    external: true
  }
}`,...(c=(o=r.parameters)==null?void 0:o.docs)==null?void 0:c.source}}};const d=["Link","External"];export{r as External,e as Link,d as __namedExportsOrder,p as default};
//# sourceMappingURL=Link.stories-0319231d.js.map
