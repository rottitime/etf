const c={title:"Components/ProgressBar",tags:["autodocs"],render:({level:m,type:p,maximum:d})=>`
    <div class="${p}">
    ${[...Array(d).keys()].map(l=>`<div class="square ${l<m?"filled":""}"></div>`).join("")}
      </div>

    `,argTypes:{maximum:{table:{disable:!0}},level:{control:{type:"range",min:0,max:5}}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/2ZaOCrzk941el36zvdgSHA/Evaluation-Registry?type=design&node-id=443-11663&t=myY59OmXjRW0K1yQ-0"},docs:{description:{component:"A progress bar to indicate the current phase of the service."}}}},e={args:{level:2,type:"progress-bar-horizontal-wide",maximum:5}},r={args:{...e.args,type:"progress-bar-horizontal",maximum:7},argTypes:{level:{control:{type:"range",min:0,max:7}}}};var a,s,n;e.parameters={...e.parameters,docs:{...(a=e.parameters)==null?void 0:a.docs,source:{originalSource:`{
  args: {
    level: 2,
    type: 'progress-bar-horizontal-wide',
    maximum: 5
  }
}`,...(n=(s=e.parameters)==null?void 0:s.docs)==null?void 0:n.source}}};var t,o,i;r.parameters={...r.parameters,docs:{...(t=r.parameters)==null?void 0:t.docs,source:{originalSource:`{
  args: {
    ...Standard.args,
    type: 'progress-bar-horizontal',
    maximum: 7
  },
  argTypes: {
    level: {
      control: {
        type: 'range',
        min: 0,
        max: 7
      }
    }
  }
}`,...(i=(o=r.parameters)==null?void 0:o.docs)==null?void 0:i.source}}};const g=["Standard","Mini"];export{r as Mini,e as Standard,g as __namedExportsOrder,c as default};
//# sourceMappingURL=ProgressBar.stories-37fe1dcc.js.map
