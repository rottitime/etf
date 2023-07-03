import{c as b}from"./utils-f016dfc5.js";const v={title:"Components/Button",tags:["autodocs"],render:h=>b(h),argTypes:{label:{control:"text"},onClick:{action:"onClick",table:{disable:!0}},small:{control:"boolean"}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-388&t=wYAx110qILxbxZUz-0"},docs:{description:{component:`Use the button component to help users carry out an action like starting an application or saving their information.
## When to use this component
Services must use the phase banner until they pass a live assessment.
Use an alpha banner when your service is in alpha, and a beta banner if your service is in private or public beta.

##How it works
Button text should be written in sentence case and describe the action it performs. For instance:



 ##Primary buttons
On a page, ensure that the main call to action is represented by a primary button. It is not recommended to have multiple primary buttons on a single page, as having more than one main call to action can lessen their effectiveness. This can confuse users and make it difficult for them to determine what action to take next.`}}}},e={args:{label:"Button"}},a={args:{...e.args,category:"secondary"}},r={args:{...e.args,category:"tertiary"}},t={args:{...e.args,category:"negative"}};var n,s,o;e.parameters={...e.parameters,docs:{...(n=e.parameters)==null?void 0:n.docs,source:{originalSource:`{
  args: {
    label: 'Button'
  }
}`,...(o=(s=e.parameters)==null?void 0:s.docs)==null?void 0:o.source}}};var i,c,m;a.parameters={...a.parameters,docs:{...(i=a.parameters)==null?void 0:i.docs,source:{originalSource:`{
  args: {
    ...Primary.args,
    category: 'secondary'
  }
}`,...(m=(c=a.parameters)==null?void 0:c.docs)==null?void 0:m.source}}};var p,l,u;r.parameters={...r.parameters,docs:{...(p=r.parameters)==null?void 0:p.docs,source:{originalSource:`{
  args: {
    ...Primary.args,
    category: 'tertiary'
  }
}`,...(u=(l=r.parameters)==null?void 0:l.docs)==null?void 0:u.source}}};var g,d,y;t.parameters={...t.parameters,docs:{...(g=t.parameters)==null?void 0:g.docs,source:{originalSource:`{
  args: {
    ...Primary.args,
    category: 'negative'
  }
}`,...(y=(d=t.parameters)==null?void 0:d.docs)==null?void 0:y.source}}};const w=["Primary","Secondary","Tertiary","Negative"];export{t as Negative,e as Primary,a as Secondary,r as Tertiary,w as __namedExportsOrder,v as default};
//# sourceMappingURL=Button.stories-b9240c36.js.map
