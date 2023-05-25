import type { StoryObj, Meta } from '@storybook/html'
import {
  Checkbox,
  createFieldset,
  createFormGroup,
  createCheckbox,
  Fieldset
} from '../utils'

type Props = { checkboxList: string[] } & Fieldset & Checkbox

const meta = {
  title: 'Components/Form/Checkbox',
  tags: ['autodocs'],
  render: ({ legend, checkboxList, ...args }) =>
    createFieldset(
      createFormGroup(
        checkboxList.map((text) =>
          createCheckbox({ ...args, name: 'radio-example', text })
        ),
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
    checkboxList: [...Array(5).keys()].map((i) => `Option ${i}`)
  }
}
