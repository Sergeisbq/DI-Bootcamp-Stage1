export const searchRobot = (resSrc) => {
  return {
    type: 'SEARCH_ROBOT',
    payload: resSrc
  }
};

export const getRobots = (data) => {
  return {
    type: 'GET_ROBOTS',
    payload: data
  }
};