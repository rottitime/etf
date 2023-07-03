var w={iphone5:{name:"iPhone 5",styles:{height:"568px",width:"320px"},type:"mobile"},iphone6:{name:"iPhone 6",styles:{height:"667px",width:"375px"},type:"mobile"},iphone6p:{name:"iPhone 6 Plus",styles:{height:"736px",width:"414px"},type:"mobile"},iphone8p:{name:"iPhone 8 Plus",styles:{height:"736px",width:"414px"},type:"mobile"},iphonex:{name:"iPhone X",styles:{height:"812px",width:"375px"},type:"mobile"},iphonexr:{name:"iPhone XR",styles:{height:"896px",width:"414px"},type:"mobile"},iphonexsmax:{name:"iPhone XS Max",styles:{height:"896px",width:"414px"},type:"mobile"},iphonese2:{name:"iPhone SE (2nd generation)",styles:{height:"667px",width:"375px"},type:"mobile"},iphone12mini:{name:"iPhone 12 mini",styles:{height:"812px",width:"375px"},type:"mobile"},iphone12:{name:"iPhone 12",styles:{height:"844px",width:"390px"},type:"mobile"},iphone12promax:{name:"iPhone 12 Pro Max",styles:{height:"926px",width:"428px"},type:"mobile"},ipad:{name:"iPad",styles:{height:"1024px",width:"768px"},type:"tablet"},ipad10p:{name:"iPad Pro 10.5-in",styles:{height:"1112px",width:"834px"},type:"tablet"},ipad12p:{name:"iPad Pro 12.9-in",styles:{height:"1366px",width:"1024px"},type:"tablet"},galaxys5:{name:"Galaxy S5",styles:{height:"640px",width:"360px"},type:"mobile"},galaxys9:{name:"Galaxy S9",styles:{height:"740px",width:"360px"},type:"mobile"},nexus5x:{name:"Nexus 5X",styles:{height:"660px",width:"412px"},type:"mobile"},nexus6p:{name:"Nexus 6P",styles:{height:"732px",width:"412px"},type:"mobile"},pixel:{name:"Pixel",styles:{height:"960px",width:"540px"},type:"mobile"},pixelxl:{name:"Pixel XL",styles:{height:"1280px",width:"720px"},type:"mobile"}};const P=[...Array(3).keys()].map(a=>({text:`Link ${a}`,href:"#"})),v={title:"Components/Header",tags:["autodocs"],render:({links:a,title:x,loggedIn:y,primaryCta:g,logout:c})=>`
      <header id="main-header">
        <div class="container">
          <a href="/" class="logo">
            <gov-icon key="crest"></gov-icon>
            <h2 class="body-text">${x}</h2>
          </a>

          ${y?`
          <button id="main-header-mobile-menu">
            <span></span>
          </button>

          <nav id="main-header-menu">
            ${a.map(({text:u,href:b})=>`<a href="${b}">${u}</a>`).join("")}

            <a class="bttn-primary" href="#">${g}</a>
            <a href="#">${c}</a>
          </nav>`:""}
        </div>
      </header>
    `,argTypes:{title:{control:"text"},primaryCta:{control:"text"},logout:{control:"text"},loggedIn:{control:"boolean",table:{disable:!0}}},parameters:{viewpoert:{viewports:w,defaultViewport:"desktop"},backgrounds:{default:"light grey"},design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-291&t=NMzWF77GnAa7BvPp-0"},docs:{description:{component:"The ETF header with navigation and user account controls."}}}},t={args:{title:"Evaluation Registry"}},e={args:{title:"Evaluation Registry",primaryCta:"Create an evaluation",logout:"Logout",loggedIn:!0,links:P}},i={...e,parameters:{viewport:{defaultViewport:"mobile1"}}};var o,n,s;t.parameters={...t.parameters,docs:{...(o=t.parameters)==null?void 0:o.docs,source:{originalSource:`{
  args: {
    title: 'Evaluation Registry'
  }
}`,...(s=(n=t.parameters)==null?void 0:n.docs)==null?void 0:s.source}}};var p,r,l;e.parameters={...e.parameters,docs:{...(p=e.parameters)==null?void 0:p.docs,source:{originalSource:`{
  args: {
    title: 'Evaluation Registry',
    primaryCta: 'Create an evaluation',
    logout: 'Logout',
    loggedIn: true,
    links
  }
}`,...(l=(r=e.parameters)==null?void 0:r.docs)==null?void 0:l.source}}};var h,m,d;i.parameters={...i.parameters,docs:{...(h=i.parameters)==null?void 0:h.docs,source:{originalSource:`{
  ...Authenticated,
  parameters: {
    viewport: {
      defaultViewport: 'mobile1'
    }
  }
}`,...(d=(m=i.parameters)==null?void 0:m.docs)==null?void 0:d.source}}};const f=["Default","Authenticated","Mobile"];export{e as Authenticated,t as Default,i as Mobile,f as __namedExportsOrder,v as default};
//# sourceMappingURL=Header.stories-5ab8d189.js.map
