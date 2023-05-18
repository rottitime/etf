import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  copywright: string
  links: string[]
}

const links = [...Array(3).keys()].map((i) => `Link ${i}`)

const meta = {
  title: 'Components/Footer',
  tags: ['autodocs'],
  render: ({ copywright, links }) =>
    `<footer class="main-footer">
    <div class="container">
       <nav>
          ${links.map((link) => `<a href="#">${link}</a>`).join('')}
       </nav>
       <div class="disclaimer">
          ${copywright} <gov-icon key='crest'></gov-icon>
       </div>
    </div>
 </footer>`,
  argTypes: {
    copywright: { control: 'text' }
  },
  parameters: {
    backgrounds: {
      default: 'light grey'
    },
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-339&t=NMzWF77GnAa7BvPp-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    copywright: '© 2021 i-AI-DS',
    links
  }
}
