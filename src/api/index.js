async function fetchAllUsers() {
  const res = await fetch('/api');
  const data = await res.json();
  return data;
}

module.exports.fetchAllUsers = fetchAllUsers;
