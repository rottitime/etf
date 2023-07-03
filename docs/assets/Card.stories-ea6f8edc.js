import{a as p}from"./utils-f016dfc5.js";import{s as g}from"./card-dcddfdb7.js";const h={title:"Components/Card",tags:["autodocs"],render:m=>p(m).outerHTML,argTypes:{title:{control:"text",description:"title for the card"},content:{control:"text",name:"content",description:" card content"},actions:{control:"boolean",table:{disable:!0}},small:{control:"boolean"},onClick:{action:"clicked",table:{disable:!0}}},parameters:{backgrounds:{default:"light grey"},design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=481-545&t=FJwPXpig0RTCQXW7-0"},docs:{description:{component:"Cards are used to present content in an organized and concise manner."}}}},e={args:{title:"Card component",content:"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rutrum mollis eros, at luctus ligula tincidunt eget. Maecenas lacus diam, dapibus id condimentum a, congue venenatis neque. Aenean lobortis molestie risus, sit amet vehicula tellus iaculis maximus. Nulla eros orci, interdum sed est in, lobortis eleifend erat. Vivamus et dictum risus. Phasellus gravida pharetra lectus, sed varius lectus posuere ac. Integer molestie purus quis quam imperdiet tincidunt.",small:!1}},t={args:{...e.args,actions:!0}},s={args:{...e.args,accordion:!0,open:!0},loaders:[async()=>setTimeout(()=>Promise.resolve(g()))]};var r,a,o;e.parameters={...e.parameters,docs:{...(r=e.parameters)==null?void 0:r.docs,source:{originalSource:`{
  args: {
    title: 'Card component',
    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rutrum mollis eros, at luctus ligula tincidunt eget. Maecenas lacus diam, dapibus id condimentum a, congue venenatis neque. Aenean lobortis molestie risus, sit amet vehicula tellus iaculis maximus. Nulla eros orci, interdum sed est in, lobortis eleifend erat. Vivamus et dictum risus. Phasellus gravida pharetra lectus, sed varius lectus posuere ac. Integer molestie purus quis quam imperdiet tincidunt.',
    small: false
  }
}`,...(o=(a=e.parameters)==null?void 0:a.docs)==null?void 0:o.source}}};var i,n,u;t.parameters={...t.parameters,docs:{...(i=t.parameters)==null?void 0:i.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    actions: true
  }
}`,...(u=(n=t.parameters)==null?void 0:n.docs)==null?void 0:u.source}}};var c,l,d;s.parameters={...s.parameters,docs:{...(c=s.parameters)==null?void 0:c.docs,source:{originalSource:`{
  args: {
    ...Default.args,
    accordion: true,
    open: true
  },
  //reload the accordion setup for cards
  loaders: [async () => {
    return setTimeout(() => Promise.resolve(setupCards()));
  }]
}`,...(d=(l=s.parameters)==null?void 0:l.docs)==null?void 0:d.source}}};const v=["Default","WithButtons","WithAccordion"];export{e as Default,s as WithAccordion,t as WithButtons,v as __namedExportsOrder,h as default};
//# sourceMappingURL=Card.stories-ea6f8edc.js.map
