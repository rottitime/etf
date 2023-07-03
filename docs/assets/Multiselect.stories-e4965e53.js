import{g as T,h as x}from"./utils-f016dfc5.js";const m=[...Array(20).keys()].map(s=>`Option ${s}`),D={title:"Components/Form/Multiselect",tags:["autodocs"],render:({error:s,label:f,description:g,helperText:h,...b})=>T(x(b),{error:s,label:f,description:g,helperText:h}).outerHTML,argTypes:{name:{control:"text",table:{disable:!0}},fullWidth:{control:"boolean"},disabled:{control:"boolean",defaultValue:!1},onchange:{action:"changed",table:{disable:!0}}}},e={args:{name:"my-select",list:m,fullWidth:!0,disabled:!1}},r={args:{...e.args,disabled:!0}},a={args:{...e.args,label:"Type of problem",helperText:"This is a invalid choice",description:"A description helps users understand the context of the field",value:m[1],error:!0}};var t,o,l;e.parameters={...e.parameters,docs:{...(t=e.parameters)==null?void 0:t.docs,source:{originalSource:`{
  args: {
    name: 'my-select',
    list,
    fullWidth: true,
    disabled: false
  }
}`,...(l=(o=e.parameters)==null?void 0:o.docs)==null?void 0:l.source}}};var n,i,c;r.parameters={...r.parameters,docs:{...(n=r.parameters)==null?void 0:n.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    disabled: true
  }
}`,...(c=(i=r.parameters)==null?void 0:i.docs)==null?void 0:c.source}}};var d,u,p;a.parameters={...a.parameters,docs:{...(d=a.parameters)==null?void 0:d.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    label: 'Type of problem',
    helperText: 'This is a invalid choice',
    description: 'A description helps users understand the context of the field',
    value: list[1],
    error: true
  }
}`,...(p=(u=a.parameters)==null?void 0:u.docs)==null?void 0:p.source}}};const S=["Default","Disabled","Error"];export{e as Default,r as Disabled,a as Error,S as __namedExportsOrder,D as default};
//# sourceMappingURL=Multiselect.stories-e4965e53.js.map
