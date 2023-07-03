import{g as b,k as D}from"./utils-f016dfc5.js";const y={title:"Components/Form/Textarea",tags:["autodocs"],render:({error:u,label:m,description:g,helperText:h,...f})=>b(D(f),{error:u,label:m,description:g,helperText:h}),argTypes:{fullWidth:{control:"boolean"},placeholder:{control:"text"},onkeyup:{action:"changed",table:{disable:!0}}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=481-954&t=suZkdl8uVnyH6HpY-0"}}},e={args:{label:"Short descritpion",placeholder:"e.g. Describe your problem here"}},r={args:{...e.args,helperText:"Only user letters and not numbers",description:"A description helps users understand the context of the field"}},t={args:{...r.args,error:!0}};var s,a,o;e.parameters={...e.parameters,docs:{...(s=e.parameters)==null?void 0:s.docs,source:{originalSource:`{
  args: {
    label: 'Short descritpion',
    placeholder: 'e.g. Describe your problem here'
  }
}`,...(o=(a=e.parameters)==null?void 0:a.docs)==null?void 0:o.source}}};var n,c,i;r.parameters={...r.parameters,docs:{...(n=r.parameters)==null?void 0:n.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    helperText: 'Only user letters and not numbers',
    description: 'A description helps users understand the context of the field'
  }
}`,...(i=(c=r.parameters)==null?void 0:c.docs)==null?void 0:i.source}}};var l,p,d;t.parameters={...t.parameters,docs:{...(l=t.parameters)==null?void 0:l.docs,source:{originalSource:`{
  args: {
    ...Description.args,
    error: true
  }
}`,...(d=(p=t.parameters)==null?void 0:p.docs)==null?void 0:d.source}}};const S=["Default","Description","Error"];export{e as Default,r as Description,t as Error,S as __namedExportsOrder,y as default};
//# sourceMappingURL=Textarea.stories-1d6e7a88.js.map
