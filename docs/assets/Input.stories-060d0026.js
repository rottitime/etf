import{g as v,f as O}from"./utils-f016dfc5.js";import{f as k}from"./utils-8fe55ea7.js";const A={title:"Components/Form/Input",tags:["autodocs"],loaders:[async()=>setTimeout(()=>{Promise.resolve(k())})],render:({error:Y,label:w,description:S,helperText:D,...T})=>v(O(T),{error:Y,label:w,description:S,helperText:D}),argTypes:{placeholder:{control:"text",description:"Lower color contrast and disappears when users start writing in the field. But if the text contains instructional info or examples which vanish, it can hinder users from confirming their responses before submitting the form."},fullWidth:{control:"boolean"},error:{control:"boolean"},label:{control:"text"},helperText:{control:"text"},description:{control:"text"},onkeyup:{action:"changed",table:{disable:!0}},dimension:{control:{type:"select"},options:["small","medium","large"]}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=27-75&t=ur05zeF7bSVeJzta-0"},docs:{description:{component:`Standard input field
##When to use this component
If you need users to input short text such as their name or phone number that doesn't exceed a single line, then you should opt for the text input component.
##How it works
You should have labels for all text inputs, and generally, it's recommended to keep them visible. Labels should be positioned above the respective text input and must be concise, straightforward, and written in sentence case. Avoid using colons at the end of the labels.`}}}},r={args:{placeholder:"e.g. Joe Blogs",dimension:"medium",type:"text",label:"Your name"}},e={args:{...r.args,helperText:"Only user letters and not numbers",description:"A description helps users understand the context of the field"}},t={args:{className:"search-icon",placeholder:"Search keywords...",fullWidth:!0}},s={args:{...e.args,error:!0}},o={args:{...e.args,label:"Year",helperText:"Only use numbers in format of YYYY",maxLength:4,placeholder:"e.g. 2021",type:"number"}};var n,a,i;r.parameters={...r.parameters,docs:{...(n=r.parameters)==null?void 0:n.docs,source:{originalSource:`{
  args: {
    placeholder: 'e.g. Joe Blogs',
    dimension: 'medium',
    type: 'text',
    label: 'Your name'
  }
}`,...(i=(a=r.parameters)==null?void 0:a.docs)==null?void 0:i.source}}};var c,l,d;e.parameters={...e.parameters,docs:{...(c=e.parameters)==null?void 0:c.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    helperText: 'Only user letters and not numbers',
    description: 'A description helps users understand the context of the field'
  }
}`,...(d=(l=e.parameters)==null?void 0:l.docs)==null?void 0:d.source}}};var p,u,m;t.parameters={...t.parameters,docs:{...(p=t.parameters)==null?void 0:p.docs,source:{originalSource:`{
  args: {
    className: 'search-icon',
    placeholder: 'Search keywords...',
    fullWidth: true
  }
}`,...(m=(u=t.parameters)==null?void 0:u.docs)==null?void 0:m.source}}};var h,g,f;s.parameters={...s.parameters,docs:{...(h=s.parameters)==null?void 0:h.docs,source:{originalSource:`{
  args: {
    ...Description.args,
    error: true
  }
}`,...(f=(g=s.parameters)==null?void 0:g.docs)==null?void 0:f.source}}};var b,x,y;o.parameters={...o.parameters,docs:{...(b=o.parameters)==null?void 0:b.docs,source:{originalSource:`{
  args: {
    ...Description.args,
    label: 'Year',
    helperText: 'Only use numbers in format of YYYY',
    maxLength: 4,
    placeholder: 'e.g. 2021',
    type: 'number'
  }
}`,...(y=(x=o.parameters)==null?void 0:x.docs)==null?void 0:y.source}}};const I=["Default","Description","Search","Error","Year"];export{r as Default,e as Description,s as Error,t as Search,o as Year,I as __namedExportsOrder,A as default};
//# sourceMappingURL=Input.stories-060d0026.js.map
