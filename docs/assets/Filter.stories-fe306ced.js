import{s as d,a as h}from"./filters-accordion-adfd64e7.js";import{s as i}from"./utils-8fe55ea7.js";const m=[...Array(4).keys()].map(e=>`Option ${e}`),l=[...Array(3).keys()].map(e=>({title:`Option ${e}`,options:m})),f={title:"Components/Filter",tags:["autodocs"],loaders:[async()=>setTimeout(()=>{Promise.resolve(d()),Promise.resolve(h())})],render:({title:e})=>`
    
    <div class="search-filters">
      <header>
        <h3 class="highlight header5">${e}</h3>
      </header>
      <ul class="accordion">

        ${l.map(({title:t,options:c},p)=>`
            <li>
              <h3 ${p===0?'aria-selected="true"':""}>
                <button type="button">
                  <span class="title">${t}</span>
                </button>
              </h3>
              <div class="accordion-content">
                <fieldset class="filter-control">
                  <div class="mb-16">
                    <input type="text" placeholder="Filter..." class="small full-width mb-8" data-controls="${i(t)}">
                    <button type="reset" class="txt-link small" disabled>Reset</button>
                  </div>
                  <div class="scroll">
                    ${c.map(o=>`<label class="checkbox">
                    <input name="${i(t)}"  type="checkbox" value="${o}">
                    <span class="checkmark"></span>
                    <span>${o}</span>
                    </label>`).join("")}
                  </div>
                </fieldset>
              </div>
            </li>
            `).join("")}
      </ul>
      </div>
    
    `,argTypes:{},parameters:{backgrounds:{default:"light grey"},design:{type:"figma",url:"https://www.figma.com/file/2ZaOCrzk941el36zvdgSHA/Evaluation-Registry?type=design&node-id=53-2331&t=gNsXGm9Pr2IQAxj3-0"},docs:{description:{component:`Allows the users select one or more options by using the checkboxes component.

## When to use this component
Use the checkboxes component when you need to help users:
- select multiple options from a list
- toggle a single option on or off

##How it works
To ensure maximum accessibility, checkboxes should be positioned to the left of their corresponding labels. This is particularly helpful for users of screen magnifiers.

While radios only allow for a single selection, checkboxes permit choosing multiple options from a list. Avoid assuming that users can determine the number of options they may select based purely on the designs of radios and checkboxes.

Consider providing a "Select all that apply" prompt or other hints to clarify the available selections.

Pre-selecting checkbox options might increase the likelihood of user errors such as missing a question or submitting an incorrect answer. Thus, it's best to avoid pre-selecting options.

By default, arrange checkbox options alphabetically to ensure consistency in selection order.`}}}},s={args:{title:"Filters",filterList:l}};var r,a,n;s.parameters={...s.parameters,docs:{...(r=s.parameters)==null?void 0:r.docs,source:{originalSource:`{
  args: {
    title: 'Filters',
    filterList
  }
}`,...(n=(a=s.parameters)==null?void 0:a.docs)==null?void 0:n.source}}};const b=["PhaseBanner"];export{s as PhaseBanner,b as __namedExportsOrder,f as default};
//# sourceMappingURL=Filter.stories-fe306ced.js.map
