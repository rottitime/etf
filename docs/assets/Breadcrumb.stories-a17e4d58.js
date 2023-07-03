const c=[{text:"Home",href:"#"},{text:"Food",href:"#"},{text:"Fruit",href:"#"}],l={title:"Components/Breadcrumb",tags:["autodocs"],render:({links:r,activeLink:a})=>`
    <nav aria-label="Breadcrumb" class="breadcrumb">
    <ol>
      ${r&&r.map(({text:o,href:i})=>`<li><a href="${i}">${o}</a></li>`).join("")}
      ${a?`<li aria-current="true">${a}</li>`:""}
      
    </ol>
  </nav>

   
    `,argTypes:{},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=485-752&t=lsxxoIbrtlv60JJm-0"},docs:{description:{component:"The breadcrumbs component helps users to understand where they are within a website’s structure and move between levels of the within a navigational hierarchy."}}}},e={args:{links:c,activeLink:"Apples"}};var t,s,n;e.parameters={...e.parameters,docs:{...(t=e.parameters)==null?void 0:t.docs,source:{originalSource:`{
  args: {
    links,
    activeLink: 'Apples'
  }
}`,...(n=(s=e.parameters)==null?void 0:s.docs)==null?void 0:n.source}}};const d=["Breadcrumb"];export{e as Breadcrumb,d as __namedExportsOrder,l as default};
//# sourceMappingURL=Breadcrumb.stories-a17e4d58.js.map
