var y=(e=>(e[e.header1=0]="header1",e[e.header2=1]="header2",e[e.header3=2]="header3",e[e.header4=3]="header4",e[e.header5=4]="header5",e))(y||{});const x={title:"Atoms/Headings",tags:["autodocs"],render:({label:e,heading:v,highlight:w})=>`<h1 class="${v}${w?" highlight":""}">${e}</h1>`,argTypes:{label:{control:"text"},highlight:{control:"boolean"},heading:{control:{type:"select"},options:Object.values(y).filter(e=>isNaN(Number(e)))}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=480-386&t=NMzWF77GnAa7BvPp-0"}}},a={args:{label:"Header 01",heading:"header1",highlight:!1}},r={args:{...a.args,label:"Header 02",heading:"header2"}},s={args:{...a,label:"Header 03",heading:"header3"}},d={args:{...a,label:"Header 04",heading:"header4"}},o={args:{...a,label:"Header 05",heading:"header5"}};var n,t,h;a.parameters={...a.parameters,docs:{...(n=a.parameters)==null?void 0:n.docs,source:{originalSource:`{
  args: {
    label: 'Header 01',
    heading: 'header1',
    highlight: false
  }
}`,...(h=(t=a.parameters)==null?void 0:t.docs)==null?void 0:h.source}}};var l,c,g;r.parameters={...r.parameters,docs:{...(l=r.parameters)==null?void 0:l.docs,source:{originalSource:`{
  args: {
    ...Header1.args,
    label: 'Header 02',
    heading: 'header2'
  }
}`,...(g=(c=r.parameters)==null?void 0:c.docs)==null?void 0:g.source}}};var i,p,m;s.parameters={...s.parameters,docs:{...(i=s.parameters)==null?void 0:i.docs,source:{originalSource:`{
  args: {
    ...Header1,
    label: 'Header 03',
    heading: 'header3'
  }
}`,...(m=(p=s.parameters)==null?void 0:p.docs)==null?void 0:m.source}}};var u,H,b;d.parameters={...d.parameters,docs:{...(u=d.parameters)==null?void 0:u.docs,source:{originalSource:`{
  args: {
    ...Header1,
    label: 'Header 04',
    heading: 'header4'
  }
}`,...(b=(H=d.parameters)==null?void 0:H.docs)==null?void 0:b.source}}};var f,S,N;o.parameters={...o.parameters,docs:{...(f=o.parameters)==null?void 0:f.docs,source:{originalSource:`{
  args: {
    ...Header1,
    label: 'Header 05',
    heading: 'header5'
  }
}`,...(N=(S=o.parameters)==null?void 0:S.docs)==null?void 0:N.source}}};const A=["Header1","Header2","Header3","Header4","Header5"];export{a as Header1,r as Header2,s as Header3,d as Header4,o as Header5,A as __namedExportsOrder,x as default};
//# sourceMappingURL=Heading.stories-e2781573.js.map
