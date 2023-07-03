var p=(e=>(e.Pink="",e.Purple="purple",e.Green="green",e.Orange="orange",e))(p||{});const m={title:"Components/Chip",tags:["autodocs"],render:({color:e,label:u,hasClose:h})=>{const t=document.createElement("div");if(t.classList.add("chip"),t.innerText=u,e&&t.classList.add(e),h){const a=document.createElement("a");a.setAttribute("title","close"),a.classList.add("close"),a.innerHTML='<gov-icon key="cross"></gov-icon>',t.appendChild(a)}return t},argTypes:{label:{control:"text"},hasClose:{control:"boolean",table:{disable:!0}},color:{control:{type:"select"},options:p}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=30-100&t=5eFOsFvCi3xiEsBW-0"},docs:{description:{component:`A divider to separate content.
##When to use this component
Use the chip component when it’s possible for something to have more than one status and it’s useful for the user to know about that status. For example, you can use a chip to show whether an item in a task list has been ‘completed’.

##How it works

Chips are used solely for indicating the status of an item, and so links should not be added to them. When naming your chips, it's recommended to use adjectives instead of verbs. The use of verbs may lead a user to believe that clicking on a chip will perform an action.`}}}},s={args:{label:"My chip"}},o={args:{...s.args,hasClose:!0}};var n,r,i;s.parameters={...s.parameters,docs:{...(n=s.parameters)==null?void 0:n.docs,source:{originalSource:`{
  args: {
    label: 'My chip'
  }
}`,...(i=(r=s.parameters)==null?void 0:r.docs)==null?void 0:i.source}}};var c,l,d;o.parameters={...o.parameters,docs:{...(c=o.parameters)==null?void 0:c.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    hasClose: true
  }
}`,...(d=(l=o.parameters)==null?void 0:l.docs)==null?void 0:d.source}}};const g=["Default","WithClose"];export{s as Default,o as WithClose,g as __namedExportsOrder,m as default};
//# sourceMappingURL=Chip.stories-fc152a69.js.map
