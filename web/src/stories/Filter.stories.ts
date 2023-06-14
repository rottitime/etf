import type { StoryObj, Meta } from '@storybook/html'
import setupFilters from '../components/filters'
import setupFiltersAccordion from '../components/filters-accordion'

import { slugify } from '../components/utils'

type Props = {
  title: string
  filterList: {
    title: string
    options: string[]
  }[]
}

const options = [...Array(4).keys()].map((i) => `Option ${i}`)

const filterList = [...Array(3).keys()].map((i) => ({ title: `Option ${i}`, options }))

const meta = {
  title: 'Components/Filter',
  tags: ['autodocs'],
  loaders: [
    async () => {
      return setTimeout(() => {
        Promise.resolve(setupFilters())
        Promise.resolve(setupFiltersAccordion())
      })
    }
  ],
  render: ({ title }) =>
    `
    
    <div class="search-filters">
      <header>
        <h3 class="highlight header5">${title}</h3>
      </header>
      <ul class="accordion">

        ${filterList
          .map(
            ({ title, options }, i) => `
            <li>
              <h3 ${i === 0 ? 'aria-selected="true"' : ''}>
                <button type="button">
                  <span class="title">${title}</span>
                </button>
              </h3>
              <div class="accordion-content">
                <fieldset class="filter-control">
                  <div class="mb-16">
                    <input type="text" placeholder="Filter..." class="small full-width mb-8" data-controls="${slugify(
                      title
                    )}">
                    <button type="reset" class="txt-link small" disabled>Reset</button>
                  </div>
                  <div class="scroll">
                    ${options
                      .map(
                        (option) => `<label class="checkbox">
                    <input name="${slugify(title)}"  type="checkbox" value="${option}">
                    <span class="checkmark"></span>
                    <span>${option}</span>
                    </label>`
                      )
                      .join('')}
                  </div>
                </fieldset>
              </div>
            </li>
            `
          )
          .join('')}
      </ul>
      </div>
    
    `,
  argTypes: {},
  parameters: {
    backgrounds: {
      default: 'light grey'
    },
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/2ZaOCrzk941el36zvdgSHA/Evaluation-Registry?type=design&node-id=53-2331&t=gNsXGm9Pr2IQAxj3-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const PhaseBanner: Story = {
  args: {
    title: 'Filters',
    filterList
  }
}
