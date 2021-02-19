/*
 * Complete the 'getArticleTitles' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts STRING author as parameter.
 *
 * URL for cut and paste:
 * https://jsonmock.hackerrank.com/api/articles?author=<authorName>&page=<num>
 *
 */

async function getArticleTitles(author) {
  let titlesArr = [];
  let page = 1;
  function getArticles(link) {
    return new Promise((resolve, reject) => {
      https.get(link, (res) => {
        let data = [];
        res
          .on("data", (d) => {
            data.push(d);
          })
          .on("error", (e) => {
            reject(e);
          })
          .on("end", () => {
            let buffer = Buffer.concat(data);
            resolve(JSON.parse(buffer.toString()));
          });
      });
    });
  }

  let link = `https://jsonmock.hackerrank.com/api/articles?author=${author}&page=${page}`;

  const articles = await getArticles(link);

  const { data, total_pages } = articles;

  for (let i = 0; i < data.length; i++) {
    let curr = data[i];
    if (curr.title || curr.story_title) {
      titlesArr.push(curr.title ? curr.title : curr.story_title);
    }
  }

  if (total_pages > 1) {
    page += 1;
    while (page <= total_pages) {
      link = `https://jsonmock.hackerrank.com/api/articles?author=${author}&page=${page}`;
      const { data: newData } = await getArticles(link);
      for (let i = 0; i < newData.length; i++) {
        let curr = newData[i];
        if (curr.title || curr.story_title) {
          titlesArr.push(curr.title ? curr.title : curr.story_title);
        }
      }
      page += 1;
    }
  }
  return titlesArr;
}
