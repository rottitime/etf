import{f as s}from"./utils-f016dfc5.js";const d={title:"Components/Form/Date Picker",tags:["autodocs"],render:r=>{const t=document.createElement("div");return t.classList.add("date-picker"),t.appendChild(s(r)),t},argTypes:{fullWidth:{control:"boolean"},value:{control:"text"},onkeyup:{action:"changed",table:{disable:!0}},type:{control:"text",defaultValue:"date",table:{disable:!0}},dimension:{control:{type:"select"},options:["small","medium","large"]}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=27-75&t=ur05zeF7bSVeJzta-0"},docs:{description:{component:`The date input component helps users enter a memorable date or one they can easily look up. 
##When to use this component
Use the date input component when you’re asking users for a date they’ll already know, or can look up without using a calendar.

##When not to use this component
Do not use the date input component if users are unlikely to know the exact date of the event you’re asking about.`}}}},e={args:{type:"date",dimension:"medium"}};var o,n,a;e.parameters={...e.parameters,docs:{...(o=e.parameters)==null?void 0:o.docs,source:{originalSource:`{
  args: {
    type: 'date',
    dimension: 'medium'
  }
}`,...(a=(n=e.parameters)==null?void 0:n.docs)==null?void 0:a.source}}};const c=["DatePicker"];export{e as DatePicker,c as __namedExportsOrder,d as default};
//# sourceMappingURL=DatePicker.stories-a59c05eb.js.map
