import type { StoryObj, Meta } from '@storybook/html'
import { createFieldset, createFormGroup, createRadio, Fieldset, Radio } from '../utils'

type Props = { radioList: string[]; otherText?: string } & Fieldset & Radio

const meta = {
  title: 'Components/Form/Radio',
  tags: ['autodocs'],
  render: ({ legend, radioList, ...args }) =>
    createFieldset(
      createFormGroup(
        radioList.map((text) => createRadio({ ...args, name: 'radio-example', text })),
        {}
      ),
      legend
    ),
  argTypes: {
    legend: { control: 'text' },
    large: { control: 'boolean' },
    onkeyup: { action: 'changed', table: { disable: true } }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=32-159&t=s7R0duWzGfG8Vf2S-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    legend: 'Pick a option',
    radioList: [...Array(5).keys()].map((i) => `Option ${i}`)
  }
}
