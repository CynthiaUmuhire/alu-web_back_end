export default function hasValuesFromArray(set, values) {
  let result = true;
  for (const value of values) {
    if (!set.has(value)) {
      result = false;
    }
  }

  return result;
}
