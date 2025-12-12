
export const MAIN_PALETTE = [
  '#03045E', // Deep Blue
  '#D84315', // Deep Orange
  '#2E7D32', // Green
  '#F9A825', // Yellow
  '#6A1B9A', // Purple
  '#00838F', // Cyan
  '#AD1457', // Pink
  '#283593', // Indigo
  '#4E342E', // Brown
  '#455A64', // Blue Grey
  '#C62828', // Red
  '#0277BD', // Light Blue
  '#9E9D24', // Lime
];

export const colorUtils = {
  // Lighten a color by percentage
  lighten: (hex: string, percent: number): string => {
    const num = parseInt(hex.replace('#', ''), 16)
    const amt = Math.round(2.55 * percent)
    const R = (num >> 16) + amt
    const G = (num >> 8 & 0x00FF) + amt
    const B = (num & 0x0000FF) + amt
    return '#' + (0x1000000 + (R < 255 ? R < 1 ? 0 : R : 255) * 0x10000 +
      (G < 255 ? G < 1 ? 0 : G : 255) * 0x100 +
      (B < 255 ? B < 1 ? 0 : B : 255)).toString(16).slice(1)
  },

  desaturate: (hex: string, percent: number): string => {
    const num = parseInt(hex.replace('#', ''), 16)
    const R = num >> 16
    const G = num >> 8 & 0x00FF
    const B = num & 0x0000FF
    const gray = R * 0.299 + G * 0.587 + B * 0.114
    const factor = percent / 100
    const newR = Math.round(R * (1 - factor) + gray * factor)
    const newG = Math.round(G * (1 - factor) + gray * factor)
    const newB = Math.round(B * (1 - factor) + gray * factor)
    return '#' + (0x1000000 + newR * 0x10000 + newG * 0x100 + newB).toString(16).slice(1)
  }
};

export const applyPaletteToData = (data: any[]) => {
  let mainColorIndex = 0

  const applyColors = (items: any[], level: number = 0, parentColor?: string) => {
    return items.map((item, index) => {
      let color: string
      
      if (level === 0) {
        // Root node (Level 0) - "AI Safety"
        color = '#ffffff'; 
      } else if (level === 1) {
        // Main Sections (Level 1) - Assign from Palette
        color = MAIN_PALETTE[mainColorIndex % MAIN_PALETTE.length]
        mainColorIndex++
      } else if (level >= 2 && parentColor) {
        // Agendas (Level 2+) - Derive from Parent
        if (item.isExtension) {
          // If it's an extension node, make it invisible (opacity 0)
          // We keep the color logic just in case, but it won't be seen
          color = parentColor;
        } else {
          // Otherwise vary lightness slightly to distinguish adjacent sectors
          const lightenAmount = 5 + (index % 3) * 5
          color = colorUtils.lighten(parentColor, lightenAmount)
        }
      } else {
        color = '#666666'
      }

      const newItem = {
        ...item,
        itemStyle: { 
          // Merge existing style if any (e.g. from dataProcessing)
          ...item.itemStyle,
          // Enforce our calculated opacity/color
          ...(item.isExtension ? { color, opacity: 0 } : { color, opacity: 1 }),
          // For the center node, ensure opacity 1
          ...(level === 0 ? { opacity: 1 } : {})
        },
      }
      
      if (item.children) {
        newItem.children = applyColors(item.children, level + 1, color)
      }
      
      return newItem
    })
  }
  
  return applyColors(data)
}
