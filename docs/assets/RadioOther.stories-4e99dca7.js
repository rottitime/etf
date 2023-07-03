const t={title:"Components/Form/Radio/Other",render:({otherLabel:l})=>`<div class="form-group">
  <label class="radio">
    <input type="radio" name="measure_type" value="CONTINUOUS">
    <span class="checkmark"></span>
    <span>Continuous</span>
  </label>
  <label class="radio">
    <input type="radio" name="measure_type" value="DISCRETE">
    <span class="checkmark"></span>
    <span>Discrete</span>
  </label>
  <label class="radio">
    <input type="radio" name="measure_type" value="BINARY">
    <span class="checkmark"></span>
    <span>Binary</span>
  </label>
  <label class="radio">
    <input type="radio" name="measure_type" value="ORDINAL">
    <span class="checkmark"></span>
    <span>Ordinal</span>
  </label>
  <label class="radio">
    <input type="radio" name="measure_type" value="NOMINAL">
    <span class="checkmark"></span>
    <span>Nominal</span>      
  </label>
  <label class="radio">
    <input type="radio" name="measure_type" value="OTHER" aria-controls="conditional-7b4039ab" checked>
    <span class="checkmark"></span>
    <span>Other</span>
  </label>
  <div class="form-group controller-subfield" id="conditional-7b4039ab">
    <label for="measure_type_other">${l}</label>
    <textarea placeholder="" id="measure_type_other" name="measure_type_other" class="full-width"></textarea>
  </div>

</div>`,argTypes:{otherLabel:{control:"text",description:"Label for the other text input",name:"Other label"}},parameters:{design:{type:"figma",url:"https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=32-159&t=s7R0duWzGfG8Vf2S-0"}}},a={args:{otherLabel:"Please provide more detail"}};var e,s,r;a.parameters={...a.parameters,docs:{...(e=a.parameters)==null?void 0:e.docs,source:{originalSource:`{
  args: {
    otherLabel: 'Please provide more detail'
  }
}`,...(r=(s=a.parameters)==null?void 0:s.docs)==null?void 0:r.source}}};const n=["Other"];export{a as Other,n as __namedExportsOrder,t as default};
//# sourceMappingURL=RadioOther.stories-4e99dca7.js.map
