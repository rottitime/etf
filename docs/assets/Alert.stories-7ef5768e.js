var l=(r=>(r[r.Success=0]="Success",r[r.Error=1]="Error",r[r.Warning=2]="Warning",r))(l||{});const h={title:"Components/Alert",tags:["autodocs"],render:({text:r,status:t})=>`<div class="alert ${t==null?void 0:t.toLowerCase()}">${r}</div>`,argTypes:{status:{control:{type:"select"},options:Object.values(l).filter(r=>isNaN(Number(r)))}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=488-791&t=5eFOsFvCi3xiEsBW-0"},docs:{description:{component:"Alert components are used to display important messages or notifications to users. These alerts are often used to convey critical information such as errors, warnings, and updates related to the system or content being viewed. The alert component is designed to grab the user's attention and provide a clear and concise message with appropriate action steps or instructions if required."}}}},e={args:{text:"This is an error alert — check it out!",status:"Success"}},s={args:{...e.args,status:"Error"}},a={args:{...e.args,status:"Warning"}};var o,n,c;e.parameters={...e.parameters,docs:{...(o=e.parameters)==null?void 0:o.docs,source:{originalSource:`{
  args: {
    text: 'This is an error alert — check it out!',
    status: 'Success'
  }
}`,...(c=(n=e.parameters)==null?void 0:n.docs)==null?void 0:c.source}}};var i,d,p;s.parameters={...s.parameters,docs:{...(i=s.parameters)==null?void 0:i.docs,source:{originalSource:`{
  args: {
    ...Success.args,
    status: 'Error'
  }
}`,...(p=(d=s.parameters)==null?void 0:d.docs)==null?void 0:p.source}}};var g,u,m;a.parameters={...a.parameters,docs:{...(g=a.parameters)==null?void 0:g.docs,source:{originalSource:`{
  args: {
    ...Success.args,
    status: 'Warning'
  }
}`,...(m=(u=a.parameters)==null?void 0:u.docs)==null?void 0:m.source}}};const f=["Success","Error","Warning"];export{s as Error,e as Success,a as Warning,f as __namedExportsOrder,h as default};
//# sourceMappingURL=Alert.stories-7ef5768e.js.map
