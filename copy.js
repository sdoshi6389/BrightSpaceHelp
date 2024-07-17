//Works for scraping the blockchain course and only that course, all other courses give an error when scanning for their content (courseContentTitles)

const puppeteer = require('puppeteer');
const fs = require('fs').promises;

(async () => {
  const url = 'https://purdue.brightspace.com/d2l/lp/auth/saml/initiate-login?entityId=https://idp.purdue.edu/idp/shibboleth&amp;target=%2fd2l%2fhome%2f6824';
  const username = 'doshi50';
  const password = '#Sinmaster23';
  var desiredURL = 'https://purdue.brightspace.com/d2l/home/6824';

  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto(url);

  await page.waitForSelector('#username', { visible: true });
  await page.type('#username', username);
  await page.waitForSelector('#password', { visible: true });
  await page.type('#password', password);
  await page.click("button[name='_eventId_proceed'].btn.btn-dark.px-5.rounded-0");

  // Wait for the desired URL or a specific condition
  let navigationComplete = false;

  const waitForDesiredURL = async () => {
    await page.waitForNavigation({ waitUntil: 'networkidle0' });
    const currentURL = page.url();
    if (currentURL.includes(desiredURL)) {
      console.log('Navigated to the desired URL');
      navigationComplete = true;
    } else {
      console.log('Current URL:', currentURL);
      console.log('Waiting for the desired URL...');
      if (!navigationComplete) {
        await waitForDesiredURL(); // Recursive call to wait for the desired URL
      }
    }
  };

  await waitForDesiredURL();

  // Array of references for each course, add this on to the original brightspace url
  const enrollmentCardsRef = await page.evaluate(() => {
    const cards = document.querySelector('body').querySelector('.d2l-body-main-wrapper')
      .querySelector('.d2l-page-main.d2l-max-width.d2l-min-width').querySelector('.d2l-page-main-padding')
      .querySelector('.d2l-homepage').querySelector('.homepage-container')
      .querySelector('.homepage-col-8').querySelector('.d2l-widget.d2l-tile')
      .querySelector('.d2l-widget-content').querySelector('.d2l-widget-content-padding')
      .querySelector('.d2l-my-courses-widget.d2l-token-receiver').shadowRoot
      .querySelector('d2l-my-courses-container').shadowRoot.querySelector('d2l-tabs')
      .querySelector('d2l-tab-panel').querySelector('d2l-my-courses-content').shadowRoot
      .querySelector('d2l-my-courses-card-grid').shadowRoot.querySelector('.course-card-grid.columns-2')
      .querySelectorAll('d2l-enrollment-card');
    
    return Array.from(cards).map(card => card.shadowRoot.querySelector('d2l-card').href);
  });

  const enrollmentCardsRefFileName = "enrollmentCardsRef.txt";

  async function clearAndAppendToEnrollmentCardRefFile() {
    try {
      // Clear the file contents
      await fs.writeFile(enrollmentCardsRefFileName, '');
      console.log('File contents have been cleared');

      // Append each card to the file
      for (const card of enrollmentCardsRef) {
        console.log(card);
        console.log('---');
        await fs.appendFile(enrollmentCardsRefFileName, card + '\n');
        console.log("File has been appended");
      }
    } catch (err) {
      console.error("Error writing to file", err);
    }
  }

  clearAndAppendToEnrollmentCardRefFile();

  // Array of names for each course
  const enrollmentCardsNames = await page.evaluate(() => {
    const cards = document.querySelector('body').querySelector('.d2l-body-main-wrapper')
      .querySelector('.d2l-page-main.d2l-max-width.d2l-min-width').querySelector('.d2l-page-main-padding')
      .querySelector('.d2l-homepage').querySelector('.homepage-container')
      .querySelector('.homepage-col-8').querySelector('.d2l-widget.d2l-tile')
      .querySelector('.d2l-widget-content').querySelector('.d2l-widget-content-padding')
      .querySelector('.d2l-my-courses-widget.d2l-token-receiver').shadowRoot
      .querySelector('d2l-my-courses-container').shadowRoot.querySelector('d2l-tabs')
      .querySelector('d2l-tab-panel').querySelector('d2l-my-courses-content').shadowRoot
      .querySelector('d2l-my-courses-card-grid').shadowRoot.querySelector('.course-card-grid.columns-2')
      .querySelectorAll('d2l-enrollment-card');
    
    return Array.from(cards).map(card => card.shadowRoot.querySelector('d2l-card').text);
  });

  const courseNamesFileName = "courseNames.txt";

  async function clearAndAppendToCourseNamesFile() {
    try {
      // Clear the file contents
      await fs.writeFile(courseNamesFileName, '');
      console.log('File contents have been cleared');

      // Append each card to the file
      for (const card of enrollmentCardsNames) {
        console.log(card);
        console.log('---');
        await fs.appendFile(courseNamesFileName, card + '\n');
        console.log("File has been appended");
      }
    } catch (err) {
      console.error("Error writing to file", err);
    }
  }

  clearAndAppendToCourseNamesFile();

  //we will loop this with all the different enrollment card references as these are 
  //the different courses
  const courseHomeUrl = 'https://purdue.brightspace.com' + enrollmentCardsRef[0];

  await page.goto(courseHomeUrl, { waitUntil: 'networkidle0' });
  const newCurrentURL = page.url();
  console.log("Current url is: ", newCurrentURL);

  //this gives us the links to all the different parts of the course page
  //such as content, classlist, etc
  const courseOptionReferences = await page.evaluate(() => {
    const headers = document.querySelectorAll('.d2l-navigation-s-item');

    return Array.from(headers).map(header => header.firstChild.href);
  });

  const courseHeaderTabLinksFileName = "course1HeaderTabLinks.txt"; //the number will be the index of the for loop plus 1 when looping through multiple courses

  async function clearAndAppendToCourseHeaderTabLinksFile() {
    try {
      // Clear the file contents
      await fs.writeFile(courseHeaderTabLinksFileName, '');
      console.log('File contents have been cleared');

      // Append each card to the file
      for (const header of courseOptionReferences) {
        console.log(header);
        console.log('---');
        await fs.appendFile(courseHeaderTabLinksFileName, header + '\n');
        console.log("File has been appended");
      }
    } catch (err) {
      console.error("Error writing to file", err);
    }
  }

  clearAndAppendToCourseHeaderTabLinksFile();

  //will need to do this for all the different links that come from
  //the course option references, this is just the first page (there should be 5)
  await page.goto(courseOptionReferences[0], { waitUntil: 'networkidle0' });
  const newCurrentURL2 = page.url();
  console.log("Current url is: ", newCurrentURL2);

  const courseAnnouncements = await page.evaluate (() => {
    const announcements = document.querySelector('d2l-expand-collapse-content')
    .querySelector('.d2l-widget-content-padding').querySelector('.d2l-placeholder.d2l-placeholder-live')
    .querySelector('div').querySelector('div').querySelector('ul').querySelectorAll('li');

    return Array.from(announcements).map(announcement => announcement.firstElementChild.lastElementChild.firstElementChild.innerHTML);
  });

  const courseAnnouncementsFileName = "course1Announcements.txt"; 

  async function clearAndAppendToCourseAnnouncementsFile() {
    try {
      // Clear the file contents
      await fs.writeFile(courseAnnouncementsFileName, '');
      console.log('File contents have been cleared');

      // Append each card to the file
      for (const announcements of courseAnnouncements) {
        console.log(announcements);
        console.log('---');
        await fs.appendFile(courseAnnouncementsFileName, announcements + '\n');
        console.log("File has been appended");
      }
    } catch (err) {
      console.error("Error writing to file", err);
    }
  }

  clearAndAppendToCourseAnnouncementsFile();

  const courseAnnouncementHeaders = await page.evaluate (() => {
    const announcementHeaders = document.querySelector('d2l-expand-collapse-content')
    .querySelector('.d2l-widget-content-padding').querySelector('.d2l-placeholder.d2l-placeholder-live')
    .querySelector('div').querySelector('div').querySelector('ul').querySelectorAll('li');

    return Array.from(announcementHeaders).map(announcementHeader => announcementHeader.innerText);
  });

  const courseAnnouncementHeadersFileName = "course1AnnouncementHeaders.txt"; 

  async function clearAndAppendToCourseAnnouncementHeadersFile() {
    try {
      // Clear the file contents
      await fs.writeFile(courseAnnouncementHeadersFileName, '');
      console.log('File contents have been cleared');

      // Append each card to the file
      for (const announcementHeader of courseAnnouncementHeaders) {
        console.log(announcementHeader);
        console.log('---');
        await fs.appendFile(courseAnnouncementHeadersFileName, announcementHeader + '\n');
        console.log("File has been appended");
      }
    } catch (err) {
      console.error("Error writing to file", err);
    }
  }

  clearAndAppendToCourseAnnouncementHeadersFile();

  const courseContentUrl = courseOptionReferences[1];

  await page.goto(courseContentUrl, { waitUntil: 'networkidle0' });
  const newCurrentURL3 = page.url();
  console.log("Current url is: ", newCurrentURL3);


  const courseHeaders = await page.evaluate (() => {
    const headers = document.querySelector('.d2l-datalist.vui-list').querySelectorAll('.d2l-datalist-item.d2l-datalist-item-hide-separators.d2l-datalist-simpleitem');

    return Array.from(headers).map(header => header.firstElementChild.firstElementChild.lastElementChild.firstElementChild.outerText)
  }); 

  console.log('<<<<<');
  console.log(courseHeaders);
  console.log('<<<<<')

  const courseHeadersFileName = "course1Headers.txt"; 

  async function clearAndAppendToCourseHeadersFile() {
    try {
      // Clear the file contents
      await fs.writeFile(courseHeadersFileName, '');
      console.log('File contents have been cleared');

      // Append each card to the file
      for (const header of courseHeaders) {
        console.log(header);
        console.log('---');
        await fs.appendFile(courseHeadersFileName, header + '\n');
        console.log("File has been appended");
      }
    } catch (err) {
      console.error("Error writing to file", err);
    }
  }

  clearAndAppendToCourseHeadersFile();

  // courseHeaders.forEach(header => {
  //   console.log(header);
  //   console.log('---');
  // });

  const courseContentTitles = await page.evaluate(() => {
    const titles = document.querySelector('.d2l-datalist.vui-list').querySelectorAll('.d2l-datalist-item.d2l-datalist-item-hide-separators.d2l-datalist-simpleitem');
    
    const aElements = [];
    
    titles.forEach(title => {
      const aElement = title.firstElementChild.firstElementChild.lastElementChild.lastElementChild.firstElementChild
      .firstElementChild.firstElementChild.firstElementChild.lastElementChild.querySelectorAll('.d2l-datalist-item.d2l-datalist-simpleitem');
      
      const temp = [];

      aElement.forEach(element => {
        temp.push(element.querySelector('a').outerHTML);
      });

      aElements.push(temp);
    });
    
    return aElements;
  });

  const courseContentFileName = "course1Content.txt"; 

  async function clearAndAppendToCourseContentFile() {
    try {
      // Clear the file contents
      await fs.writeFile(courseContentFileName, '');
      console.log('File contents have been cleared');

      // Append each card to the file
      for (const content of courseContentTitles) {
        console.log(content);
        console.log('---');
        await fs.appendFile(courseContentFileName, content.toString() + '\n');
        console.log("File has been appended");
      }
    } catch (err) {
      console.error("Error writing to file", err);
    }
  }
  
  clearAndAppendToCourseContentFile();

  // console.log(courseContentTitles);

  await page.goto(courseOptionReferences[3], { waitUntil: 'networkidle0' });
  const newCurrentURL4 = page.url();
  console.log("Current url is: ", newCurrentURL4);

  const courseGrades = await page.evaluate(() => {
    const gradesArray = document.querySelector('tbody').querySelectorAll('tr');

    const gradeElements = [];

    gradesArray.forEach(grade => {
      const gradeRow = grade.childNodes;

      const temp = [];

      gradeRow.forEach(element => {
        temp.push(element.innerText);
      });

      gradeElements.push(temp);
    });

    return gradeElements;
  });

  const courseGradesFileName = "course1Grades.txt"; 

  async function clearAndAppendToCourseGradesFile() {
    try {
      // Clear the file contents
      await fs.writeFile(courseGradesFileName, '');
      console.log('File contents have been cleared');

      // Append each card to the file
      for (const grade of courseGrades) {
        console.log(grade);
        console.log('---');
        await fs.appendFile(courseGradesFileName, grade.toString() + '\n');
        console.log("File has been appended");
      }
    } catch (err) {
      console.error("Error writing to file", err);
    }
  }
  
  clearAndAppendToCourseGradesFile();

  //console.log(courseGrades);


  //keeps the brwoser open
  await new Promise(resolve => {});

  await browser.close();
})();
