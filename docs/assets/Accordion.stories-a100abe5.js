import{s as v,a as y}from"./filters-accordion-adfd64e7.js";const O="lo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget",a=[...Array(3).keys()].map(o=>({title:`Title ${o}`,open:!1,content:O})),w={title:"Components/Accordion",tags:["autodocs"],loaders:[async()=>setTimeout(()=>{Promise.resolve(v()),Promise.resolve(y())})],render:({list:o,openAll:g})=>`<div is="idotai-accordion">

    ${o.map(({title:A,content:f,open:S})=>`
      <div class="accordion-title"${g||S?" aria-expanded='true'":""}>
        <h3 class="body-text">${A}</h3>
      </div>
      <div class="accordion-panel">
      <p>${f}</p>
      </div>
    `).join("")}
</div>



    
    `,argTypes:{},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=53-609&t=oaVjP0J6w3Dd6kBW-0"}}},e={args:{openAll:!1,list:a}},s={args:{openAll:!1,list:[...a.slice(0,1),{...a[1],open:!0},...a.slice(2)]}},r={args:{...e.args,openAll:!0}};var t,n,i;e.parameters={...e.parameters,docs:{...(t=e.parameters)==null?void 0:t.docs,source:{originalSource:`{
  args: {
    openAll: false,
    list
  }
}`,...(i=(n=e.parameters)==null?void 0:n.docs)==null?void 0:i.source}}};var l,c,p;s.parameters={...s.parameters,docs:{...(l=s.parameters)==null?void 0:l.docs,source:{originalSource:`{
  args: {
    openAll: false,
    list: [...list.slice(0, 1), {
      ...list[1],
      open: true
    }, ...list.slice(2)]
  }
}`,...(p=(c=s.parameters)==null?void 0:c.docs)==null?void 0:p.source}}};var d,m,u;r.parameters={...r.parameters,docs:{...(d=r.parameters)==null?void 0:d.docs,source:{originalSource:`{
  args: {
    ...Standard.args,
    openAll: true
  }
}`,...(u=(m=r.parameters)==null?void 0:m.docs)==null?void 0:u.source}}};const x=["Standard","SingleOpen","AllOpen"];export{r as AllOpen,s as SingleOpen,e as Standard,x as __namedExportsOrder,w as default};
//# sourceMappingURL=Accordion.stories-a100abe5.js.map
