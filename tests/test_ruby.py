import unittest
import textwrap
from pseudon import generate
from pseudon.pseudon_tree import Node
import suite

#v
class TestRuby(unittest.TestCase, metaclass=suite.TestLanguage): # dark magic bitches
    
    _language = 'ruby'
    _import = 'require'
    _parse_import = lambda self, line: line[9:-1]

    # make declarative style great again

    # expected ruby translation for each example in suite:

    int_ = '42'

    float_ = '42.42'

    string = "'la'"

    boolean = 'true'

    null = 'nil'

    dictionary = "{la: 0}"

    list_ = "['la']"

    local = 'egg'

    typename = 'Egg'

    instance_variable = '@egg'

    attr = 'e.egg'

    local_assignment = 'egg = ham'

    instance_assignment = '@egg = ham'

    attr_assignment = 'T.egg = ham'

    call = 'map(x)'

    method_call = 'e.filter(42)'

    standard_call = [
        'puts 42',
        'gets',
        'Math.log(ham)',
        "File.read('f.py')"
    ]

    standard_method_call = [
        'l.length',
        "'l'[0...2]"
    ]

    binary_op = 'ham + egg'

    unary_op = '-a'

    comparison = 'egg > ham'

    if_statement = textwrap.dedent('''\
        if egg == ham
          l[0...2]
        elsif egg == ham
          4.2
        else
          z
        end''')

    for_each_statement = textwrap.dedent('''\
        sequence.each do |a|
          a.sub
        end''')

    for_range = textwrap.dedent('''\
        (0...42).step(2).each do |j|
          analyze(j)
        end''')

    for_each_with_index = [
        textwrap.dedent('''\
          z.each_with_index do |k, j|
            analyze(j, k)
          end'''),

        textwrap.dedent('''\
          z.each do |j, k|
            analyze(j, k)
          end''')
    ]

    for_each_in_zip = textwrap.dedent('''\
        z.zip(zz).each do |k, l|
          a(k, l)
        end''')

    while_statement = textwrap.dedent('''\
        while f() >= 42
          b = g
        end''')

    function_definition = textwrap.dedent('''\
        def weird(z)
          fixed = fix(z)
          fixed
        end''')

    method_definition = textwrap.dedent('''\
        def parse(source)
          @ast = nil
          [source]
        end''')

    anonymous_function = [
        '-> source { ves(source.length) }',

        textwrap.dedent('''\
            -> source do
              puts source
              ves(source)
            end''')
    ]

    class_statement = [textwrap.dedent('''\
        class A < B
          def initialize(a)
            @a = a
          end

          def parse
            42
          end
        end''')]

    this = 'self'

    constructor = textwrap.dedent('''\
        def initialize(a, b)
          @a = a
          @b = b
        end''')

    index = "'la'[2]"

    index_assignment = "x[4] = 'String'"

    try_statement = [
        textwrap.dedent('''\
            begin
              a
              h(-4)
            rescue StandardError => e
              puts e
            end'''),

        textwrap.dedent('''\
            class NeptunError < StandardError
            end

            begin
              a
              h(-4)
            resuce NeptunError => e
              echo e
            end''')
    ]

    throw_statement = textwrap.dedent('''\
        class NeptunError < StandardError
        end

        throw NeptunError.new(\'no tea\')''')



