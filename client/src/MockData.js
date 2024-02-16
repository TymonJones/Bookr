import faker from 'faker';

const generateListings = (count) => {
  const listings = [];
  for (let i = 0; i < count; i++) {
    const listing = {
      id: i + 1,
      title: faker.lorem.words(3),
      description: faker.lorem.paragraph(),
      price: faker.random.number({ min: 50, max: 500 }),
      bedrooms: faker.random.number({ min: 1, max: 5 }),
      bathrooms: faker.random.number({ min: 1, max: 3 }),
      guests: faker.random.number({ min: 1, max: 10 }),
      amenities: [
        faker.random.arrayElement(['Wi-Fi', 'Pool', 'Gym', 'Kitchen', 'Parking']),
        faker.random.arrayElement(['Wi-Fi', 'Pool', 'Gym', 'Kitchen', 'Parking']),
        faker.random.arrayElement(['Wi-Fi', 'Pool', 'Gym', 'Kitchen', 'Parking'])
      ],
      rating: faker.random.number({ min: 3, max: 5, precision: 0.1 }),
      reviews: faker.random.number({ min: 10, max: 200 }),
      imageUrl: faker.image.imageUrl()
    };
    listings.push(listing);
  }
  return listings;
};

const MockData = {
  listings: generateListings(10),
};

export default MockData;
