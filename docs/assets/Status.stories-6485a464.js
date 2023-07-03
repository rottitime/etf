var B=(e=>(e.Default="",e.Green="green",e.Orange="orange",e.Red="red",e.Blue="blue",e))(B||{});const x={title:"Components/Status",tags:["autodocs"],render:({color:e,label:w})=>{const a=document.createElement("div");return a.classList.add("chip"),a.setAttribute("role","status"),a.innerText=w,e&&a.classList.add(e.toLowerCase()),a},argTypes:{label:{control:"text"},color:{control:{type:"select"},options:B}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=30-100&t=5eFOsFvCi3xiEsBW-0"},docs:{description:{component:"To show the status of an item."}}}},r={args:{label:"My chip"}},s={args:{...r.args,color:"Green"}},t={args:{...r.args,color:"Orange"}},o={args:{...r.args,color:"Red"}},n={args:{...r.args,color:"Blue"}};var c,l,d;r.parameters={...r.parameters,docs:{...(c=r.parameters)==null?void 0:c.docs,source:{originalSource:`{
  args: {
    label: 'My chip'
  }
}`,...(d=(l=r.parameters)==null?void 0:l.docs)==null?void 0:d.source}}};var u,p,g;s.parameters={...s.parameters,docs:{...(u=s.parameters)==null?void 0:u.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    color: 'Green'
  }
}`,...(g=(p=s.parameters)==null?void 0:p.docs)==null?void 0:g.source}}};var i,m,f;t.parameters={...t.parameters,docs:{...(i=t.parameters)==null?void 0:i.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    color: 'Orange'
  }
}`,...(f=(m=t.parameters)==null?void 0:m.docs)==null?void 0:f.source}}};var D,O,h;o.parameters={...o.parameters,docs:{...(D=o.parameters)==null?void 0:D.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    color: 'Red'
  }
}`,...(h=(O=o.parameters)==null?void 0:O.docs)==null?void 0:h.source}}};var S,b,y;n.parameters={...n.parameters,docs:{...(S=n.parameters)==null?void 0:S.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    color: 'Blue'
  }
}`,...(y=(b=n.parameters)==null?void 0:b.docs)==null?void 0:y.source}}};const G=["Default","Green","Orange","Red","Blue"];export{n as Blue,r as Default,s as Green,t as Orange,o as Red,G as __namedExportsOrder,x as default};
//# sourceMappingURL=Status.stories-6485a464.js.map
