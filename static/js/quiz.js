const myQuiz = [
    {
      'q': 'What\'s COVID-19?',
      'options': [
        'CornaVirus disease',
        'SARS disease',
        'Ebola virus',
        'None of the above'
      ],
      'correctIndex': 0,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'How long should you wash your hand?',
      'options': [
        'At least 10 sec',
        'At least 30 sec',
        'At least 20 sec',
        'At least 50 sec'
      ],
      'correctIndex': 2,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'Each of the following statements is true, except:',
      'options': [
        'Viruses come in differnet types',
        'Viruses infect living cells',
        'viruses can ruplicate without hosts',
        'Viruses can cause illnesses'
      ],
      'correctIndex': 2,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'A virus infects a host in order to:',
      'options': [
        'Take in nutrients',
        'Make the host sick',
        'Destroy the host\'s cells',
        'Make copies of itself'
      ],
      'correctIndex': 3,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'The distinguishing feature of a coronavirus is its:',
      'options': [
        'Size',
        'Mobility',
        'Shape',
        'Deadliness'
      ],
      'correctIndex': 2,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'A typical coronavirus infection:',
      'options': [
        'Has mild symptoms',
        'Is extremely dangerous',
        'Cannot spread to humans',
        'Is resistant to hand washing'
      ],
      'correctIndex': 0,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'Coronavirus infections are likely to be more serious for:',
      'options': [
        'Teens',
        'Active adults',
        'Frequent travelers',
        'People with weakened immune systems'
      ],
      'correctIndex': 3,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'An outbreak of a virus occurs when:',
      'options': [
        'Symptoms of the virus get worse',
        'The virus spreads to more than one organ',
        'Someone dies from the virus',
        'The virus spreads to more and more hosts'
      ],
      'correctIndex': 3,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'What does it mean when a city is quarantined during a virus outbreak?',
      'options': [
        'Everyone in the city is infected',
        'No one can enter or leave the city',
        'Doctors in the city are developing a cure',
        'The city’s population is immune to the virus'
      ],
      'correctIndex': 1,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'Which practice prevents the spread of germs?',
      'options': [
        'Washing your hands often',
        'Reusing the same tissue',
        'Blowing your nose',
        'Coughing into your hand'
      ],
      'correctIndex': 0,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'Covering your mouth when you cough or sneeze is recommended to:',
      'options': [
        'Get rid of germs from inside your body',
        'Prevent germs from entering your body',
        'Avoid getting other people sick',
        'Warn other people that you are sick'
      ],
      'correctIndex': 2,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    },
    {
      'q': 'The most reliable source of information about virus outbreaks is:',
      'options': [
        'News headlines',
        'The World Health Organization',
        'Social media',
        'Your peers'
      ],
      'correctIndex': 1,
      'correctResponse': 'Custom correct response.',
      'incorrectResponse': 'Custom incorrect response.'
    }

  ];

$('#quiz').quiz({
  questions: myQuiz,
});