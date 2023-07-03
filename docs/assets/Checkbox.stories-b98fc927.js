import{b as c,d as l,e as p}from"./utils-f016dfc5.js";const m={title:"Components/Form/Checkbox",tags:["autodocs"],render:({legend:o,checkboxList:a,...i})=>c(l(a.map(r=>p({...i,name:"radio-example",text:r})),{}),o),argTypes:{legend:{control:"text"},large:{control:"boolean"},onkeyup:{action:"changed",table:{disable:!0}}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=32-159&t=s7R0duWzGfG8Vf2S-0"},docs:{description:{component:`Allows users select one or more options by using the checkboxes component. 

##When to use this component
Use the checkboxes component when you need to help users:
- select multiple options from a list
- toggle a single option on or off

##How it works
To improve usability for users of screen magnifiers, it's important to position checkboxes to
the left of their labels. One key difference between checkboxes and radios is that multiple
options can be selected from a list of checkboxes. To avoid confusion, consider adding a hint 
 such as 'Select all that apply'.

To prevent any errors, avoid pre-selecting checkbox options. This can lead to users missing a 
question or submitting an incorrect answer. By default, it's recommended to order checkbox 
options alphabetically.


In certain cases, sorting options based on frequency may be helpful. For example, when asking 
'What is your nationality?', options could be ordered from most-to-least common based on population size.`}}}},e={args:{legend:"Pick a option",checkboxList:[...Array(5).keys()].map(o=>`Option ${o}`)}};var n,t,s;e.parameters={...e.parameters,docs:{...(n=e.parameters)==null?void 0:n.docs,source:{originalSource:`{
  args: {
    legend: 'Pick a option',
    checkboxList: [...Array(5).keys()].map(i => \`Option \${i}\`)
  }
}`,...(s=(t=e.parameters)==null?void 0:t.docs)==null?void 0:s.source}}};const u=["Default"];export{e as Default,u as __namedExportsOrder,m as default};
//# sourceMappingURL=Checkbox.stories-b98fc927.js.map
