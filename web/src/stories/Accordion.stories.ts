import type { StoryObj, Meta } from '@storybook/html'
import setupFilters from '../components/filters'
import setupFiltersAccordion from '../components/filters-accordion'

type Props = {
  openAll: boolean
  list: {
    title: string
    content: string
    open?: boolean
  }[]
}

const content = `lo Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget`
const list = [...Array(3).keys()].map((i) => ({
  title: `Title ${i}`,
  open: false,
  content
}))

const meta = {
  title: 'Components/Accordion',
  tags: ['autodocs'],
  loaders: [
    async () => {
      return setTimeout(() => {
        Promise.resolve(setupFilters())
        Promise.resolve(setupFiltersAccordion())
      })
    }
  ],
  render: ({ list, openAll }) =>
    `<div is="idotai-accordion">

    ${list
      .map(
        ({ title, content, open }) => `
      <div class="accordion-title"${openAll || open ? " aria-expanded='true'" : ''}>
        <h3 class="body-text">${title}</h3>
      </div>
      <div class="accordion-panel">
      <p>${content}</p>
      </div>
    `
      )
      .join('')}
</div>



    
    `,
  argTypes: {},
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=53-609&t=oaVjP0J6w3Dd6kBW-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Standard: Story = {
  args: {
    openAll: false,
    list
  }
}

export const SingleOpen: Story = {
  args: {
    openAll: false,
    list: [...list.slice(0, 1), { ...list[1], open: true }, ...list.slice(2)]
  }
}

export const AllOpen: Story = {
  args: {
    ...Standard.args,
    openAll: true
  }
}
