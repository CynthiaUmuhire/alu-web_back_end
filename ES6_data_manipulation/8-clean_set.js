export default function cleanSet(set, substring) {
  if (!set || !substring) return '';
  if (typeof set !== 'object' || typeof substring !== 'string') return '';
  return [...set].filter((el) => typeof el === 'string' && el.startsWith(substring)).map((el) => el.replace(substring, '')).join('-');
}
