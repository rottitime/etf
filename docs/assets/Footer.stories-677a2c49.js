const s=[...Array(3).keys()].map(e=>`Link ${e}`),c={title:"Components/Footer",tags:["autodocs"],render:({copywright:e,links:a})=>`<footer class="main-footer">
    <div class="container">
       <nav>
          ${a.map(i=>`<a href="#">${i}</a>`).join("")}
       </nav>
       <div class="disclaimer">
          ${e} <gov-icon key='crest'></gov-icon>
       </div>
    </div>
 </footer>`,argTypes:{copywright:{control:"text"}},parameters:{backgrounds:{default:"light grey"},design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-339&t=NMzWF77GnAa7BvPp-0"},docs:{description:{component:`The footer provides copyright, licensing and other information about your service.
## When to use this component
Use the footer at the bottom of every page of your service.

##How it works
Add a copyright notice to the footer to clarify who owns the copyright. Supports logos.
##Adding links
You can add links to:
- privacy notice
- accessibility statement
- cookies page
- terms and conditions
- other language options`}}}},o={args:{copywright:`© ${new Date().getFullYear()} i-AI-DS`,links:s}};var t,n,r;o.parameters={...o.parameters,docs:{...(t=o.parameters)==null?void 0:t.docs,source:{originalSource:`{
  args: {
    copywright: \`© \${new Date().getFullYear()} i-AI-DS\`,
    links
  }
}`,...(r=(n=o.parameters)==null?void 0:n.docs)==null?void 0:r.source}}};const p=["Default"];export{o as Default,p as __namedExportsOrder,c as default};
//# sourceMappingURL=Footer.stories-677a2c49.js.map
