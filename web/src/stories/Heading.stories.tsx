import type { StoryObj, Meta } from '@storybook/html'

enum Headings {
  header1,
  header2,
  header3,
  header4,
  header5
}

type Props = {
  heading: keyof typeof Headings
  label: string
  highlight: boolean
}

const meta = {
  title: 'Atoms/Headings',
  tags: ['autodocs'],
  render: ({ label, heading, highlight }) =>
    `<h1 class="${heading}${highlight ? ' highlight' : ''}">${label}</h1>`,
  argTypes: {
    label: { control: 'text' },
    highlight: { control: 'boolean' },
    heading: {
      control: { type: 'select' },
      options: Object.values(Headings).filter((v) => isNaN(Number(v)))
    }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=480-386&t=NMzWF77GnAa7BvPp-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Header1: Story = {
  args: {
    label: 'Header 01',
    heading: 'header1',
    highlight: false
  }
}

export const Header2: Story = {
  args: {
    ...Header1.args,
    label: 'Header 02',
    heading: 'header2'
  }
}

export const Header3: Story = {
  args: {
    ...Header1,
    label: 'Header 03',
    heading: 'header3'
  }
}

export const Header4: Story = {
  args: {
    ...Header1,
    label: 'Header 04',
    heading: 'header4'
  }
}

export const Header5: Story = {
  args: {
    ...Header1,
    label: 'Header 05',
    heading: 'header5'
  }
}
