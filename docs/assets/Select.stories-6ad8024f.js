import{g as y,j as T}from"./utils-f016dfc5.js";const m=[...Array(5).keys()].map(t=>`Option ${t}`),x={title:"Components/Form/Select",tags:["autodocs"],render:({error:t,label:g,description:f,helperText:h,...b})=>y(T(b),{error:t,label:g,description:f,helperText:h}).outerHTML,argTypes:{name:{control:"text",table:{disable:!0}},fullWidth:{control:"boolean"},disabled:{control:"boolean",defaultValue:!1},onchange:{action:"changed",table:{disable:!0}}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=316-330&t=3c3246gboAwz7S3E-0"}}},e={args:{name:"my-select",list:m}},r={args:{...e.args,label:"Type of problem",helperText:"This is a invalid choice",description:"A description helps users understand the context of the field",fullWidth:!0}},a={args:{...r.args,value:m[1],error:!0}};var s,o,n;e.parameters={...e.parameters,docs:{...(s=e.parameters)==null?void 0:s.docs,source:{originalSource:`{
  args: {
    name: 'my-select',
    list
  }
}`,...(n=(o=e.parameters)==null?void 0:o.docs)==null?void 0:n.source}}};var l,i,c;r.parameters={...r.parameters,docs:{...(l=r.parameters)==null?void 0:l.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    label: 'Type of problem',
    helperText: 'This is a invalid choice',
    description: 'A description helps users understand the context of the field',
    fullWidth: true
  }
}`,...(c=(i=r.parameters)==null?void 0:i.docs)==null?void 0:c.source}}};var d,p,u;a.parameters={...a.parameters,docs:{...(d=a.parameters)==null?void 0:d.docs,source:{originalSource:`{
  args: {
    ...Labels.args,
    value: list[1],
    error: true
  }
}`,...(u=(p=a.parameters)==null?void 0:p.docs)==null?void 0:u.source}}};const A=["Default","Labels","Error"];export{e as Default,a as Error,r as Labels,A as __namedExportsOrder,x as default};
//# sourceMappingURL=Select.stories-6ad8024f.js.map
